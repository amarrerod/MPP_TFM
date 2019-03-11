import matplotlib.pyplot as plt
import numpy as np
import csv

average_file = "../5_days/evolution/MPP_TFM_5_MOEA_D_PopSize_140_Neihb_42_days_5_MenuPlanning_100000000.bestAvgHV.evolution"
max_file = "../5_days/evolution/MPP_TFM_5_MOEA_D_PopSize_140_Neihb_42_days_5_MenuPlanning_100000000.maxHV.evolution"
min_file = "../5_days/evolution/MPP_TFM_5_MOEA_D_PopSize_140_Neihb_42_days_5_MenuPlanning_100000000.minHV.evolution"

preliminary_max_HV = "../preliminary/hypervolume/evolution/maxHV/MPP_TFM_MOEA_D_PopSize_140_Neihb_42_days_20_MenuPlanning_100000000.maxHV.evolution"
preliminary_avg_HV = "../preliminary/hypervolume/evolution/bestAvgHV/MPP_TFM_MOEA_D_PopSize_140_Neihb_42_days_20_MenuPlanning_100000000.bestAvgHV.evolution"
average_10_days_file = "../10_days/evolution/MPP_TFM_10_MOEA_D_PopSize_140_Neihb_42_days_10_MenuPlanning_100000000.bestAvgHV.evolution"
avg_40_days_file = "../40_days/evolution/MPP_TFM_40_MOEA_D_PopSize_140_Neihb_42_days_40_MenuPlanning_100000000.bestAvgHV.evolution"

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

def combine_plots(plot_title, checkpoints, datasets, colors, labels): 
    plt.style.use('seaborn-darkgrid')
    for idx, dataset in enumerate(datasets):
        plt.plot(checkpoints, dataset, scaley=True, color=colors[idx], label=labels[idx])
    plt.xlabel("Checkpoints")
    plt.ylabel("Hypervolume")
    plt.title(plot_title, loc="center", fontsize=20)
    plt.legend()
    plt.show()   

def plot_evolution(checkpoints, data, title, y_label, color):
    plt.style.use("seaborn-darkgrid")

    ax = plt.gca()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 16)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 8)
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
    checkpoints, max_preliminary = read_file(preliminary_max_HV)
    checkpoints, avg_preliminary = read_file(preliminary_avg_HV)
    checkpoints, avg_10_days = read_file(average_10_days_file)
    checkpoints, avg_40_days = read_file(avg_40_days_file)
    # plot_evolution(checkpoints, min_objectives, "HV's min values evolution over 1e8 ev", "Min HV", "orange")
    plot_evolution(checkpoints, avg_10_days, "HV's average values evolution over 1e8 ev for 10-days MPP", "Avg HV", "blue")
    # plot_evolution(checkpoints, max_objectives, "HV's max values evolution over 1e8 ev", "Max HV", "blue")
    datasets = [avg_40_days, avg_preliminary, avg_10_days, average_objectives]
    colors = ["purple", "green", "blue", "red"]
    labels = ["Avg HV for 40-days", "Avg HV for 20-days MPP", "Avg HV for 10-days MPP",  "Avg HV for 5-days MPP"]
    plot_title = "Comparison of Avg HV values for MOEA/D after 1e8 ev"
    combine_plots(plot_title, checkpoints, datasets, colors, labels)