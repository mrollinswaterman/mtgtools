import csv
import os

def read(path:str=None):
    if path is None: raise Exception("The 'read' function needs a file path!")
    filename, file_extension = os.path.splitext(path)
    if file_extension not in [".csv", ".txt"]:
        raise Exception (f"Unrecogized file of type {file_extension}. Please use '.csv' or '.txt'")
    
    master = []
    
    with open(path, 'r') as file:
        reader = csv.DictReader(file) if file_extension == ".csv" else None
        if reader:
            for row in reader:
                master.append(row["Name"])
        else:
            master = file.read().splitlines()

    if not master: raise Exception(f"{path} was an empty file and could not be read!")

    return master
