print('\n')
import sys
import os

#paths
current_dir = sys.path[0] #get current directory from system
data_dir = current_dir + '/data' #data path
modules_dir = current_dir + '/modules' #modules path

#add paths to system
sys.path.append(data_dir) #add data path to system
sys.path.append(modules_dir) #add modules path to system
nodes_file = os.path.join(data_dir, 'nodes.tsv') #validate nodes.tsv data file which is in seperate directory
edges_file = os.path.join(data_dir, 'edges.tsv')

#reading nodes
from readNodes import client, create, populateDB
from queryOne import findDiseaseById
from queryTwo import findCompoundsForDisease
# create(nodes_file, 'n')
# create(edges_file, 'e')
# populateDB()

# QUERIES:
def clear():
    os.system( 'clear' )

clear()
run = True
while run:
    num = 0
    print("[1]", "For GENERAL info on Disease")
    print("[2]", "For potential NEW drug treatment candidates for Disease")
    print("[3]", "Exit")
    num = int(input("Enter: "))
    if num == 1:
        clear()
        _id = input("Enter a Disease ID: ")
        findDiseaseById(_id)
        entry = input("Press enter to go back to main menu")
    elif num == 2:
        clear()
        _id = input("Enter a Disease ID: ")
        findCompoundsForDisease(_id)
        entry = input("Press enter to go back to main menu")
    elif num == 3:
        run = False
    else:
        clear()
    clear()
print("\nThank you for playing!\n")
    
    





# findDiseaseById("Disease::DOID:3312")
# findCompoundsForDisease("Disease::DOID:3312")

# Drop Database
# client.drop_database('HetioNet')