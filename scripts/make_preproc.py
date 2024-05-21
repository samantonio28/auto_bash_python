import sys
import os
from shutil import rmtree

if os.path.isdir("./preprocessed"):
    rmtree("./preprocessed")

os.mkdir("./preprocessed")

methods = ["main_f", "time_f", "tsc_f"]

for method in methods:
    if not os.path.isdir(f"./preprocessed/{method}"):
        os.mkdir(f"./preprocessed/{method}")
    
    for root, directories, files in os.walk(f'./data/{method}/'):
        roott = f"./preprocessed/{method}"
        for file in files:            
            path_file = os.path.join(roott, file[5:])
            if not os.path.isfile(path_file):
                if len(file[5:]) >= 4:
                    with open(path_file, "w") as to:
                        with open(os.path.join(root, file), "r") as fromm:
                            to.write(fromm.read())
            else:
                with open(path_file, "a") as to:
                    with open(os.path.join(root, file), "r") as fromm:
                        to.write(fromm.read())

parameters = ["average", "min", "max", "fst_quartile", "median", "trd_quartile"]
for ind in parameters:
    os.mkdir(f"./preprocessed/{ind}")

for method in methods:    
    for root, directories, files in os.walk(f'./preprocessed/{method}/'):
        params = []
        for file in files:
            path_file = os.path.join(root, file)
            with open(path_file, "r") as f:
                m = [int(i) for i in f]
                m = sorted(m)

                # print(path_file)
                avg = sum(m) / len(m)
                minim = min(m)
                maxim = max(m)
                
                fst_q = m[len(m) // 4]
                med = m[len(m) // 2]
                trd_q = m[3 * len(m) // 4]
                params += [[avg, minim, maxim, fst_q, med, trd_q]]
                
            for i in range(len(params)):
                with open(f"./preprocessed/average/{file}", "w") as f:
                    f.write(str(params[i][0]))
                with open(f"./preprocessed/min/{file}", "w") as f:
                    f.write(str(params[i][1]))
                with open(f"./preprocessed/max/{file}", "w") as f:
                    f.write(str(params[i][2]))
                with open(f"./preprocessed/fst_quartile/{file}", "w") as f:
                    f.write(str(params[i][3]))
                with open(f"./preprocessed/median/{file}", "w") as f:
                    f.write(str(params[i][4]))
                with open(f"./preprocessed/trd_quartile/{file}", "w") as f:
                    f.write(str(params[i][5]))
                    
sys.exit(0)