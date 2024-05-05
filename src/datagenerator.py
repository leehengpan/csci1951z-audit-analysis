import numpy as np
import pandas as pd
import json


def randomizer(init_arr=None, func=np.random.choice, seed=1951, **kwargs):
    np.random.seed(seed)
    if init_arr:
        return func(init_arr, **kwargs)
    else:
        return func(**kwargs)


def data_generator(config_file, num_rows):
    results = {}
    with open(config_file) as f:
        initializers = json.load(f)

    for key, val in initializers.items():
        if key not in ("GPA", "job_histories"):
            results[key] = randomizer(val, size=num_rows)
        if key == "GPA":
            results[key] = np.round(np.clip(randomizer(func=np.random.normal, loc=3, scale=2, size=num_rows), 0, 4), 2)
        if key == "job_histories":
            results["jobref_id"] = randomizer(init_arr=list(val.keys()), size=num_rows)
            jobref_df = pd.DataFrame.from_dict(initializers["job_histories"], orient="index")
            jobref_df.columns = ["Role 1", "Start 1", "End 1", "Role 2", "Start 2", "End 2", "Role 3", "Start 3",
                                 "End 3"]
            jobref_df.reset_index(inplace=True)
            jobref_df.rename(columns={"index": "jobref_id"}, inplace=True)

    df = pd.DataFrame(results)
    result_df = pd.merge(left=df, right=jobref_df, on=['jobref_id'])
    return result_df
