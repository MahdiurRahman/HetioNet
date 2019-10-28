print("Loading readNodes module......")

def createNodes(file_path):
    with open(file_path) as nodes:
        for line in nodes:
            print(line)