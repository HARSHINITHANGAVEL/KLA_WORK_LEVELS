import networkx as nx
import numpy as np
import json

def create_graph_from_matrix(distance_matrix):
    num_nodes = len(distance_matrix)
    G = nx.Graph()

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = distance_matrix[i][j]
            G.add_edge(i, j, weight=weight)

    return G
def save_tsp_path_to_json(path, level0_output):
    with open(level0_output, 'w') as json_file:
        json.dump(path, json_file)
def solve_tsp(graph):
   
    tsp_path = nx.approximation.traveling_salesman_problem(graph, cycle=True)
    return tsp_path
df = open('Input data/level0.json')
data = json.load(df)
distance_matrix=[]
val = []
val.append(0)

for i in (data["restaurants"]["r0"]["neighbourhood_distance"]):
    val.append(i)
print(val)
distance_matrix.append(val)
val=[]
print(data["restaurants"]["r0"]["neighbourhood_distance"][2])
for i in range(data["n_neighbourhoods"]):
    pathh = str("n")+str(i)
    val.append(data["restaurants"]["r0"]["neighbourhood_distance"][i])
    for j in data["neighbourhoods"][str(pathh)]["distances"]:
        val.append(j)
    distance_matrix.append(val)
    val=[]

weighted_graph = create_graph_from_matrix(distance_matrix)
tsp_path = solve_tsp(weighted_graph)
for i in range(len(tsp_path)) :
    if(i==0):
        tsp_path[i]=str("r")+str(tsp_path[i])
    elif(i==len(tsp_path)-1):
        tsp_path[i]=str("r")+str(tsp_path[i])
    else:
        tsp_path[i]=str("n")+str(tsp_path[i]-1)
    print(i)
print(tsp_path)

data = {
    "v0": 
        {"path": tsp_path}
    
}
save_tsp_path_to_json(data,"level0_output.json")
