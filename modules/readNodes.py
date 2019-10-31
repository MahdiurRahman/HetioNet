import csv
import time
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.HetioNet

Anatomies = db.Anatomies
Anatomies_dict = {}
Anatomies_list = []
Compounds = db.Compounds
Compounds_dict = {}
Compounds_list = []
Diseases = db.Diseases
Diseases_dict = {}
Diseases_list = []
Genes = db.Genes
Genes_dict = {}
Genes_list = []

def insertNode(row):
    node = {
        '_id': row[0],
        'name': row[1]
    }
    if row[2] == 'Anatomy':
        node.update({'upregulates': []})
        node.update({'expresses': []})
        node.update({'downregulates': []})
        Anatomies_dict[row[0]] = node
    elif row[2] == 'Compound':
        node.update({'upregulates': []})
        node.update({'binds': []})
        node.update({'downregulates': []})
        node.update({'treats': []})
        node.update({'palliates': []})
        node.update({'resembles': []})
        Compounds_dict[row[0]] = node
    elif row[2] == 'Disease':
        node.update({'upregulates': []})
        node.update({'associates': []})
        node.update({'downregulates': []})
        node.update({'localizes': []})
        node.update({'resembles': []})
        node.update({'treated_by': []})
        node.update({'palliated_by': []})
        Diseases_dict[row[0]] = node
    elif row[2] == 'Gene':
        node.update({'regulates': []})
        node.update({'interacts': []})
        node.update({'covaries': []})
        Genes_dict[row[0]] = node

def insertEdge(row):
    #Anatomy
    if row[1] == 'AuG':
        Anatomies_dict[row[0]]['upregulates'].append(row[2])
    elif row[1] == 'AeG':
        Anatomies_dict[row[0]]['expresses'].append(row[2])
    elif row[1] == 'AdG':
        Anatomies_dict[row[0]]['downregulates'].append(row[2])
        #Compounds
    elif row[1] == 'CrC':
        Compounds_dict[row[0]]['resembles'].append(row[2])
    elif row[1] == 'CtD':
        Compounds_dict[row[0]]['treats'].append(row[2])
        Diseases_dict[row[2]]['treated_by'].append(row[0])
    elif row[1] == 'CpD':
        Compounds_dict[row[0]]['palliates'].append(row[2])
        Diseases_dict[row[2]]['palliated_by'].append(row[0])
    elif row[1] == 'CuG':
        Compounds_dict[row[0]]['upregulates'].append(row[2])
    elif row[1] == 'CbG':
        Compounds_dict[row[0]]['binds'].append(row[2])
    elif row[1] == 'CdG':
        Compounds_dict[row[0]]['downregulates'].append(row[2])
        #Genes
    elif row[1] == 'Gr>G':
        Genes_dict[row[0]]['regulates'].append(row[2])
    elif row[1] == 'GcG':
        Genes_dict[row[0]]['covaries'].append(row[2])
    elif row[1] == 'GiG':
        Genes_dict[row[0]]['interacts'].append(row[2])
        #Disease
    elif row[1] == 'DrD':
        Diseases_dict[row[0]]['resembles'].append(row[2])
    elif row[1] == 'DlA':
        Diseases_dict[row[0]]['localizes'].append(row[2])
    elif row[1] == 'DuG':
        Diseases_dict[row[0]]['upregulates'].append(row[2])
    elif row[1] == 'DaG':
        Diseases_dict[row[0]]['associates'].append(row[2])
    elif row[1] == 'DdG':
        Diseases_dict[row[0]]['downregulates'].append(row[2])

def create(file_path, flag):
    with open(file_path) as nodes:
        data = csv.reader(nodes, delimiter='\t')
        rows = list(data)
        if flag == 'n':
            print("Inserting nodes...")
            start_time = time.time()
            for row in rows:
                insertNode(row)
            end_time = time.time()
            print("Finished in Seconds:", end_time - start_time)
        elif flag == 'e':
            print("Inserting edges...")
            start_time = time.time()
            for row in rows:
                insertEdge(row)
            end_time = time.time()
            print("Finished in Seconds:", end_time - start_time)
        else:
            print("You must provide correct flag 'n' or 'e'")
            return
    print('\n')
    print(Anatomies_dict['Anatomy::UBERON:0000011'])
    print(Anatomies_dict['Anatomy::UBERON:0000011']['name'])
    print('\n')

def refineData():
    for entry in Anatomies_dict:
        Anatomies_list.append(Anatomies_dict[entry])
    for entry in Compounds_dict:
        Compounds_list.append(Compounds_dict[entry])
    for entry in Diseases_dict:
        Diseases_list.append(Diseases_dict[entry])
    for entry in Genes_dict:
        Genes_list.append(Genes_dict[entry])

def populateDB():
    refineData()
    print("Starting insertion into MongoDB...")
    start_time = time.time()

    Anatomies.insert_many(Anatomies_list)
    Compounds.insert_many(Compounds_list)
    Diseases.insert_many(Diseases_list)
    Genes.insert_many(Genes_list)

    end_time = time.time()
    print("Finished")
    print('Seconds:', end_time - start_time)