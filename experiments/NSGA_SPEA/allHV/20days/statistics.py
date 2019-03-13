#!/usr/bin/python

import glob
import os
import sys
from subprocess import Popen, PIPE, STDOUT
from os import listdir
from os.path import isfile, join 
import scipy
import scipy.stats
import pandas as pd
import itertools

path = os.getcwd()
BEST = "Mejor: "
NO_DIFF = "No existe diferencia estadistica"


def get_statistics(algorithms):
    statistics = {}
    dataframe = pd.DataFrame([])
    for alg in algorithms:
        print(f"Algorithm: {alg}")
        filenames = [glob.glob(f"*{alg}*.allHV")]
        for file in filenames[0]:
            print(f"File: {file}")
            data = pd.read_csv(file)
            summary = data.describe()
            summary = summary.transpose()
            statistics[file] = summary
            print(f"Summary:\n{summary}")
            #print(f"\n\nSummary:\n {summary}\n\n")
            #lines = list(open(file))
            # for line in lines: 
            #     value = float(line.split()[0])
            #     print(f"Value: {value}")
            #     values.append(value)
            # #values = [float(x) for x, line for line in lines]
            # print(f"Values: {values}")
            # statistics[file] = values
    return statistics

def getRankings(algorithms, runs):
    rankings = {}
    filenames = [glob.glob(f"*.allHV")]
    for file_a, file_b in itertools.product(filenames[0], filenames[0]):
        if file_a != file_b:
            print(f"A: {file_a} vs  B: {file_b}")
            if file_a not in rankings:
                rankings[file_a] = [0, 0, 0, 0]
            if file_b not in rankings:
                rankings[file_b] = [0, 0, 0, 0]
            
            process = Popen(['perl', 'statisticalTests_old.pl', f'{runs}', f'{file_a}', f'{file_b}'], 
            stdout=PIPE, stderr=STDOUT)
            result = str(process.communicate()[0])
            if f'{BEST} {file_a}' in result:
                rankings[file_a][0] += 1
                rankings[file_b][1] += 1
                rankings[file_a][3] += 1
                rankings[file_b][3] -= 1
            elif f'{BEST} {file_b}' in result:
                rankings[file_b][0] += 1
                rankings[file_a][1] += 1
                rankings[file_b][3] += 1
                rankings[file_a][3] -= 1
            elif NO_DIFF in result:
                rankings[file_a][2] += 1
                rankings[file_b][2] += 1
    return rankings

def print_sorted(algs, statistics, filename): 
    to_str = f"Configuration & Min. & 1st Qu. & Std & Mean & 3rd Qu. & Max. \\\\ \\hline\n"
    #sorted_d = sorted(statistics.items(), key = lambda kv: kv[-1])
    for key in statistics:
        #data = statistics[key][["min", "25%", "std", "mean", "75%", "max"]]
        k_min = statistics[key][["min"]]
        k_first = statistics[key][["25%"]]
        k_std = statistics[key][["std"]]
        k_mean = statistics[key][["mean"]]
        k_third = statistics[key][["75%"]]
        k_max = statistics[key][["max"]]
        k_str = key.replace(".allHV", "")
        to_str += f"& {k_str} & {k_min} & {k_first} & {k_std} & {k_mean} & {k_third} & {k_max} \\\\\n"
    with open(filename, "w") as file:
        file.write(to_str)
    print(to_str)

    
if __name__ == "__main__":
    alg_1 = sys.argv[1]
    alg_2 = sys.argv[2]
    alg_3 = sys.argv[3]
    algs = [alg_1, alg_2, alg_3]
    statistics = get_statistics(algs)
    #rankings = getRankings(algs, 25)
    #print_sorted(algs, statistics, "40_stats.tex")