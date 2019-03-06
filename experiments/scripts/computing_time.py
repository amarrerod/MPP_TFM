from os import listdir
from os.path import isfile, join
import sys
import numpy as np

current_path = "/home/marrero/Universidad/MPP_TFM/experiments/scripts/temp"
pattern = "Time ="

def get_elapsed_time(filename):
    time = 0
    with open(f"{current_path}/{filename}", "r") as file:
        search_lines = file.readlines()
        for line in reversed(search_lines):
            if pattern in line:
                line = line.split()
                time = float(line[2])
                print(f"Elapsed time: {time}")
                break
    return time

if __name__ == "__main__":
   only_files = [file for file in listdir(current_path) if isfile(join(current_path, file)) and not file.endswith(".py")]
   elapsed_times = [get_elapsed_time(filename) for filename in only_files]
   av_elapsed_time = round(np.average(elapsed_times) / 3600.0, 3)
   print(f"Average elapsed time: {av_elapsed_time}")