import requests
import json
import pandas as pd


def _build_dataframe(responses):
    resp_df = pd.DataFrame()
    for resp in responses:
        resp_df = pd.concat([resp_df, pd.DataFrame(json.loads(resp.json()['prediction']))])
    return resp_df


def fetch_response(url, data, max_sz, headers={'content-type': 'application/json'}, verbose=1):
    resp_store = []
    for i in range(data.shape[0] // max_sz):
        body = json.dumps(data.iloc[i * max_sz:(i + 1) * max_sz].to_dict('records'))
        resp = requests.post(url=url, data=body, headers=headers)
        resp_store.append(resp)
        if verbose:
            print(f"Iteration {i + 1} of {data.shape[0] // max_sz} response state: {resp.ok}")
        if not resp.ok:
            print(resp.reason)
            break

    return _build_dataframe(resp_store)
