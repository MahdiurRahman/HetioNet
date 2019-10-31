import csv
import time
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.HetioNet

#Compounds
CrC = db.CrC
CtD = db.CtD
CpD = db.CpD
CuG = db.CuG
CbG = db.CbG
CdG = db.CdG
#Genes
GtD = db.CtD
GtD = db.CtD
GtD = db.CtD
#Disease
DtD = db.CtD
DtD = db.CtD
DtD = db.CtD
DtD = db.CtD
DtD = db.CtD
#Anatomy
AtD = db.CtD
AtD = db.CtD
AtD = db.CtD

def insertEdge(row):
    #Compounds
    if row[1] == 'CrC':
        print('CrC')
    elif row[1] == 'CtD':
        print('CrC')
    elif row[1] == 'CpD':
        print('CrC')
    elif row[1] == 'CuG':
        print('CbG')
    elif row[1] == 'CbG':
        print('CrC')
    elif row[1] == 'CdG':
        print('CrC')
        #Genes
    elif row[1] == 'GrG':
        print('CrC')
    elif row[1] == 'GcG':
        print('CrC')
    elif row[1] == 'GiG':
        print('CrC')
        #Disease
    elif row[1] == 'DrD':
        print('CrC')
    elif row[1] == 'DlA':
        print('CbG')
    elif row[1] == 'DuG':
        print('CrC')
    elif row[1] == 'DaG':
        print('CrC')
    elif row[1] == 'DdG':
        print('CrC')
        #Anatomy
    elif row[1] == 'AuG':
        print('CrC')
    elif row[1] == 'AeG':
        print('CrC')
    elif row[1] == 'AdG':
        print('CrC')
    

def creadeEdges(file_path):
    with open(file_path) as edges:
        data = csv.reader(edges, delimiter='\t')
        rows = list(data)
        for row in rows:
            insertEdge(row)
