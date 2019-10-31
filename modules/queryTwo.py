import time
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.HetioNet
Diseases = db["Diseases"]
Anatomies = db["Anatomies"]
Compounds = db["Compounds"]

def findDiseaseById(id):
    query = {'_id': id}
    response = Diseases.find(query)
    for disease in response:
        return disease

def findAnatomiesByList(localizations):
    response = Anatomies.find({
        "_id": {
            "$in": localizations
        }
    })
    anatomies = []
    for anatomy in response:
        anatomies.append(anatomy)
    return anatomies

def collectRegulations(anatomies, upregulations, downregulations):
    for anatomy in anatomies:
        upregulations += anatomy['upregulates']
        downregulations += anatomy['downregulates']

def collectCompounds(disease_id, upregulations, downregulations):
    response = Compounds.find({
        "$and": [
            {
                "treats": {
                    "$nin": [disease_id]
                }
            },
            {
                "upregulates": {
                    "$in": upregulations
                }
            },
            {
                "downregulates": {
                    "$in": downregulations
                }
            }
        ]
    })
    compounds = []
    for compound in response:
        compounds.append(compound)
    return compounds

def findCompoundsForDisease(id):
    # use disease to find anatomies
    disease = findDiseaseById(id)
    localizations = disease['localizes']
    anatomies = findAnatomiesByList(localizations)

    # use anatomies to find up & down reg. genes
    upregulations = []
    downregulations = []
    collectRegulations(anatomies, upregulations, downregulations)

    # use up & down reg. genes to find compounds
    compounds = collectCompounds(id, upregulations, downregulations)
    string = "Compound Candidates: "
    for compound in compounds:
        string = string + compound['name'] + ", "
    print(string)
    