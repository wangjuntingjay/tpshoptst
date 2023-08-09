import json
import os


def getdata(filepaths):
    cur_dir1 = os.path.abspath(__file__ + "/../../data")
    path1 = os.path.join(cur_dir1, filepaths)
    with open(path1, encoding="utf-8") as f:
        data = json.load(f)
        return data.values()

