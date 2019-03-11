import matplotlib.pyplot as plt
import numpy
import pandas as pd
from os import listdir
from os.path import isfile, join

current_path = "/home/marrero/Universidad/MPP_TFM/experiments/40_days/fronts"

pre_front = "../preliminary/fronts/MPP_TFM_MOEA_D_PopSize_140_Neihb_42_days_20_MenuPlanning_100000000.24_100000040.front"
main_front = "../10_days/fronts/MPP_TFM_10_MOEA_D_PopSize_140_Neihb_42_days_10_MenuPlanning_100000000.24_100000040.front"

def get_objectives(filename):
    print(f"Reading {filename}")
    objective_1 = []
    objective_2 = []
    with open(filename) as file:
        line = file.readline()
        while line:
            values = [round(float(x), 5) for x in line.split()]
            objective_1.append(values[-2])
            objective_2.append(values[-1])
            print(f"Cost: {values[-2]}, Repetition: {values[-1]}")
            line = file.readline()
    return objective_1, objective_2


def plot_front(index, title, label_x, label_y, cost, repetition, color, alg_label):
    plt.style.use("seaborn-darkgrid")
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.scatter(cost, repetition, color=color, marker="s", linewidths=2, alpha=0.9, label=alg_label)
    plt.title(title, fontsize=20)
    plt.legend()
    name = f"{alg_label}_{index}.png"
    plt.savefig(name)
    plt.clf()


if __name__ == "__main__":
    only_files = [file for file in listdir(current_path) if isfile(join(current_path, file)) and not file.endswith(".py") and not file.endswith(".png")]
    for filename in only_files:
        cost, repetition = get_objectives(filename)
        title ="Front approximations - 1e8 ev"
        label_x = "Cost"
        label_y = "Degree of repetition"
        index = filename.split("100000000.", 1)
        index = index[1].split("_100000040.front", 1)
        plot_front(index[0], title, label_x, label_y, cost, repetition, color="blue", alg_label="MOEA_D_PopSize_140_Neihb_42_days_40")
