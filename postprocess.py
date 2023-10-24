# imports
import datetime
import json
import os

def output(outputs, writeToFile, outDir="outputs"):
    json_object = json.dumps(outputs, indent = 4)

    if writeToFile:
        seconds_since_epoch = int(datetime.datetime.now().timestamp())
        fname = f"{seconds_since_epoch}.json"
        fpath = os.path.join(outDir, fname)
        if not os.path.exists(outDir):
            os.makedirs(outDir)
        with open(fpath, "w") as f:
            f.write(json_object)
    else:
        print(json_object)