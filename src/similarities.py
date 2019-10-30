import networkx as nx
import csv
from collections import Counter

class Similarities:
    def __init__(self, e_star_set, pdg, pcn, pjc, pa, ppa):
        self.e_star_set = e_star_set
        self.pdg = pdg
        self.pcn = pcn
        self.pjc = pjc
        self.pa = pa
        self.ppa = ppa
        # self.index = index

    def similarities(self):
        file = open(self.e_star_set, 'r')
        G = nx.read_adjlist(self.e_star_set)
        file.close()

        shortest_paths = nx.all_pairs_shortest_path_length(G)

        #Common Neighbors
        total_neighbors = {}
        for node in G.nodes:
            node_neighbors = G.neighbors(node)
            for node_neighbor in node_neighbors:
                if node != node_neighbor:
                    common_neighbors = nx.common_neighbors(G, node, node_neighbor)
                    total_neighbors.update({node + "," + node_neighbor: len(list(common_neighbors))})
                    for el1 in list(common_neighbors):
                        print(el1)

        totalNumberofNeighbors = int(len(total_neighbors) * (self.pcn * 0.01))
        k = Counter(total_neighbors)
        # Finding N highest values
        TopValuesOfPCN = k.most_common(totalNumberofNeighbors)
        print("This is the top " + self.pcn + "% of PCN")

        jaccard_coefficient = nx.jaccard_coefficient(G)
        adamic_adar = nx.adamic_adar_index(G)
        preferential_attachment = nx.preferential_attachment(G)

        for el in list(shortest_paths):
            print(el)






