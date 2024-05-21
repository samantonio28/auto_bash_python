import sys
import os
import matplotlib.pyplot as plt
from shutil import rmtree

methods = ["main", "time", "tsc"]
ways = ["asterisk", "pointers", "usual"]
sizes = [10, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 10000]

if len(sys.argv) == 2 and sys.argv[1] != "":
    sizes += [int(sys.argv[1])]
    sizes = sorted(sizes)

if os.path.isdir("./postproc"):
    rmtree("./postproc")

os.mkdir("./postproc")

for method in methods:
    for way in ways:
        data = []
        for size in sizes:
            with open(f"./preprocessed/average/{method}_{way}_{size}.txt", "r") as f:
                data += [float(f.readline())]
        plt.xlabel('Размер массива')
        plt.ylabel('Время сортировки')
        plt.grid()

        plt.plot(sizes, data, "*-")
    plt.legend(["asterisk", "pointers", "usual"])
    plt.savefig(f"./postproc/{method}_linear.svg")
    plt.clf()

for method in methods:
    for way in ways:
        avg = []
        maxs = []
        mins = []
        for size in sizes:
            with open(f"./preprocessed/average/{method}_{way}_{size}.txt", "r") as f:
                avg += [float(f.readline())]
            with open(f"./preprocessed/max/{method}_{way}_{size}.txt", "r") as f:
                maxs += [float(f.readline())]
            with open(f"./preprocessed/min/{method}_{way}_{size}.txt", "r") as f:
                mins += [float(f.readline())]
        plt.xlabel('Размер массива')
        plt.ylabel('Время сортировки')
        plt.grid()
        plt.errorbar(sizes, avg, yerr=[mins, maxs], fmt='*-', ecolor='red')
    plt.legend(ways)
    plt.savefig(f"./postproc/{method}_error.svg")
    plt.clf()

for method in methods:
    for way in ways:
        avg = []
        maxs = []
        mins = []
        meds = []
        fst_q = []
        trd_q = []
        for size in sizes:
            with open(f"./preprocessed/average/{method}_{way}_{size}.txt", "r") as f:
                avg += [float(f.readline())]
            with open(f"./preprocessed/max/{method}_{way}_{size}.txt", "r") as f:
                maxs += [float(f.readline())]
            with open(f"./preprocessed/min/{method}_{way}_{size}.txt", "r") as f:
                mins += [float(f.readline())]
            with open(f"./preprocessed/median/{method}_{way}_{size}.txt", "r") as f:
                meds += [float(f.readline())]
            with open(f"./preprocessed/fst_quartile/{method}_{way}_{size}.txt", "r") as f:
                fst_q += [float(f.readline())]
            with open(f"./preprocessed/trd_quartile/{method}_{way}_{size}.txt", "r") as f:
                trd_q += [float(f.readline())]
        plt.xlabel('Размер массива')
        plt.ylabel('Время сортировки')
        plt.grid()
        for i in range(len(sizes)):
            plt.boxplot([mins[i], maxs[i], fst_q[i], meds[i], trd_q[i]], positions=[sizes[i]], widths=20, showfliers=False)
    plt.legend(ways)
    plt.savefig(f"./postproc/{method}_moustache.svg")
    plt.clf()


sys.exit(0)