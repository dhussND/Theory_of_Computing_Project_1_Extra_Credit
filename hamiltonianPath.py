#!/usr/bin/env python3

import networkx as nx
import itertools
import random
import matplotlib.pyplot as plt
import time

def has_hamiltonian_path(G):
    # optimization for quickly identifying certain non-Hamiltonian graphs
    if len(list(G.edges)) < len(list(G.nodes)) - 2:
        return False
    
    # generate all permutations of the nodes
    nodes = list(G.nodes())
    for path in itertools.permutations(nodes):
        if all(G.has_edge(path[i], path[i + 1]) for i in range(len(path) - 1)):
            return True
    return False

def generate_random_graph(num_nodes):
    if num_nodes == 0:
        return nx.Graph()
    
    # random number of edges between 0 and max possible edges
    num_edges = random.randint(0, num_nodes * (num_nodes - 1) // 2)
    return nx.gnm_random_graph(num_nodes, num_edges)

# store timing and results
times = []
node_counts = []

# store colors for plotting
colors = []  

for i in range(1, 14):  # graph sizes with 1-14 nodes
    for j in range(10):  # number of graphs to be generated with _ nodes
        num_nodes = i
        G = generate_random_graph(num_nodes)
        
        start_time = time.time()  # start timing
        has_path = has_hamiltonian_path(G)
        elapsed_time = time.time() - start_time  # end timing
        
        times.append(elapsed_time)
        node_counts.append(num_nodes)

        # determine color based on Hamiltonian path status
        colors.append('green' if has_path else 'red')  # green for Hamiltonian, red for non-Hamiltonian

        if has_path:
            print(f"Hamiltonian: Nodes: {G.nodes} Edges: {G.edges}")
        else:
            print(f"Non-Hamiltonian: Nodes: {G.nodes} Edges: {G.edges}")

# display results
print(f"Graph timing results (input size vs time):")
for nodes, t, color in zip(node_counts, times, colors):
    print(f"Nodes: {nodes}, Time: {t:.6f} seconds, Color: {color}")

# plot the results
plt.figure()
# plot each point with the corresponding color
plt.scatter(node_counts, times, color=colors)

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of nodes (log scale)')
plt.ylabel('Time (seconds, log scale)')
plt.title('Hamiltonian Path Detection Time vs Number of Nodes (log-log scale)')
plt.grid(True, which="both", ls="--")

# save scatter plot to file as PNG
plt.savefig('hamiltonian_path_times.png') 
