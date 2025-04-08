import csv

file1 = "1.csv"
file2 = "2.csv"

MERGE = set()

FILE1 = []
FILE2 = []

def read_file(filename, dir):
    global MERGE
    global FILE2
    global FILE1

    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            dir.append(row["Name"])
        
        csvfile.close()

def get_unique_cards():
    global MERGE
    read_file(file1, FILE1)
    read_file(file2, FILE2)
    for idx, i in enumerate(FILE2):
        #print(FILE1[idx], i)
        if i not in FILE1:
            MERGE.add(i)

get_unique_cards()
for i in MERGE:
    print(i)
