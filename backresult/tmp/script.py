import os

f1scoredict = {}

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    k_val = str(os.path.basename(root)).split("-")[-1]
    task  = str(os.path.basename(root)).split("-")[0]
    
    if task not in f1scoredict:
        f1scoredict[task] = {}

    for file in files:
        # print(len(path) * '---', file)
        if "test_results" in str(file):
            with open(f".\{os.path.basename(root)}\{file}") as f:
                for line in f.readlines():
                    if "eval_f1" in line:
                        f1scoredict[task][k_val] = round(float(line.split("=")[-1]), 3)
import json

print(json.dumps(f1scoredict, indent=4))
                 
