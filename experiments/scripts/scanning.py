from os import listdir
from os.path import isfile, join
import re
import sys
import numpy

current_path = "/home/marrero/MPP_TFM"
pattern = "Front Size ="
only_files = [file for file in listdir(current_path) if isfile(join(current_path, file)) and not file.endswith(".py")]

obj1 = []
obj2 = []

for filename in only_files:
    print(f"Reading file {filename}...")
    lines = reversed(list(open(filename)))
    done = False
    while done is not True:
        for line in lines:
            if pattern in line:
                done = True
                print(f"Parsing file {filename} finished.\n")
                break
            else:
                values = [float(x) for x in line.split()]
                if len(values) > 0:
                    print(f"Obj1: {values[-2]}\nObj2: {values[-1]}")
                    obj1.append(values[-2])
                    obj2.append(values[-1])
                
print(f"All files have been read.")
print(f"Results: \n- Min Obj 1: {min(obj1)}\n- Max Obj 1: {max(obj1)}\n- Min Obj 2: {min(obj2)}\n- Max Obj 2: {max(obj2)}")