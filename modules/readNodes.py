import csv

def createNodes(file_path):
    with open(file_path) as nodes:
        data = csv.reader(nodes, delimiter='\t')
        rows = list(data)
        for i in range(100):
            print(i, rows[i])