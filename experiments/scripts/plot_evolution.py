import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib import gridspec
import pandas as pd

average_file = "../10_days/evolution/MPP_TFM_10_MOEA_D_PopSize_140_Neihb_42_days_10_MenuPlanning_100000000.bestAvgHV.evolution"
max_file = "../10_days/evolution/MPP_TFM_10_MOEA_D_PopSize_140_Neihb_42_days_10_MenuPlanning_100000000.maxHV.evolution"
min_file = "../10_days/evolution/MPP_TFM_10_MOEA_D_PopSize_140_Neihb_42_days_10_MenuPlanning_100000000.minHV.evolution"

def read_file(filename):
    checkpoints = []
    objectives = []
    print(f"Reading file: {filename}")
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            result = row[0].split()
            checkpoints.append(result[0])
            objectives.append(round(float(result[1]), 7))
            print(f"Checkpoint: {result[0]} value: {result[1]}")
    return checkpoints, objectives

def combine_plots(checkpoints, min, max, average): 
    plt.style.use('seaborn-darkgrid')
    plt.plot(checkpoints, min, scaley=True, color="orange", label="Min HV")
    plt.plot(checkpoints, average, scaley=True, color="green", label="Avg HV")
    plt.plot(checkpoints, max, scaley=True, color="blue", label="Max HV")
    plt.xlabel("Checkpoints")
    plt.ylabel("Hypervolume")
    plt.title("Comparison of Min, Avg and Max HV values for MOEA/D after 1e8 ev", loc="center", fontsize=20)
    plt.legend()
    plt.show()


def plot_evolution(checkpoints, data, title, y_label, color):
    plt.style.use('seaborn-darkgrid')
    plt.plot(checkpoints, data, scaley=True, color=color, label=y_label)
    plt.xlabel("Checkpoints")
    plt.ylabel(y_label)
    plt.title(title, loc="center", fontsize=20)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    checkpoints, min_objectives = read_file(min_file)
    checkpoints, average_objectives = read_file(average_file)
    checkpoints, max_objectives = read_file(max_file)
    df = pd.DataFrame({
        "x": checkpoints,
        "min": min_objectives,
        "average": average_objectives,
        "max": max_objectives
    })
    """ plot_evolution(checkpoints, min_objectives, "HV's min values evolution over 1e8 ev", "Min HV", "orange")
    plot_evolution(checkpoints, average_objectives, "HV's average values evolution over 1e8 ev", "Avg HV", "green")
    plot_evolution(checkpoints, max_objectives, "HV's max values evolution over 1e8 ev", "Max HV", "blue") """  
    combine_plots(checkpoints, min_objectives, max_objectives, average_objectives)
