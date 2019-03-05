import matplotlib.pyplot as plt
import numpy
import pandas as pd

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
    print(f"Done, length cost: {len(objective_1)}, length repetition: {len(objective_2)}")
    return objective_1, objective_2


def plot_front(title, label_x, label_y, cost, repetition, color, alg_label):
    plt.style.use("seaborn-darkgrid")
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.scatter(cost, repetition, color=color, marker="s", linewidths=2, alpha=0.9, label=alg_label)
    plt.title(title, fontsize=20)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    pre_cost, pre_rep = get_objectives(pre_front)
    main_cost, main_rep = get_objectives(main_front)
    title ="Front approximations - 1e8 ev"
    label_x = "Cost"
    label_y = "Degree of repetition"
    plot_front(title, label_x, label_y, main_cost, main_rep, color="blue", alg_label="MOEA_D_PopSize_140_Neihb_42_days_10")