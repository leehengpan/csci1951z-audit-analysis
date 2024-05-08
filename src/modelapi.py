import requests
import json
import pandas as pd
from math import ceil


def _build_dataframe(responses):
    resp_df = pd.DataFrame()
    for resp in responses:
        resp_df = pd.concat([resp_df, pd.DataFrame(json.loads(resp.json()['prediction']))])
    return resp_df


def _split_rows(num_rows, max_sz):
    start = 0
    splits = []
    while start < num_rows:
        end = start + min(num_rows - start, max_sz)
        splits.append((start, end))
        start = end
    return splits


def fetch_response(url, data, max_sz, headers={'content-type': 'application/json'}, verbose=1):
    resp_store = []
    idx_splits = _split_rows(data.shape[0], max_sz)
    for i, (start, end) in enumerate(idx_splits):
        body = json.dumps(data.iloc[start:end].to_dict('records'))
        resp = requests.post(url=url, data=body, headers=headers)
        resp_store.append(resp)
        if verbose:
            print(f"Iteration {i + 1} of {len(idx_splits)} response state: {resp.ok}")
        if not resp.ok:
            print(resp.reason)
            break

    return _build_dataframe(resp_store)
