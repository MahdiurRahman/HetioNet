import time
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.HetioNet
Diseases = db["Diseases"]

def findDiseaseById(id):
    query = {'_id': id}
    response = Diseases.find(query)
    for disease in response:
        print(disease)

def findDiseaseByName(name):
    query = {'name': name}
    response = Diseases.find(query)
    for disease in response:
        print(disease)