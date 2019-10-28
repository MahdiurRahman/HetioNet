print('\n')
import sys
import os
import neo4j

#paths
current_dir = sys.path[0] #get current directory from system
data_dir = current_dir + '/data' #data path
modules_dir = current_dir + '/modules' #modules path

#add paths to system
sys.path.append(data_dir) #add data path to system
sys.path.append(modules_dir) #add modules path to system
nodes_file = os.path.join(data_dir, 'nodes.tsv') #validate nodes.tsv data file which is in seperate directory

#reading nodes
from readNodes import createNodes
createNodes(nodes_file)