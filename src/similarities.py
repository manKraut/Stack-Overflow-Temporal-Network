import networkx as nx
import csv


class Similarities:
    def __init__(self, e_star_set):
        self.e_star_set = e_star_set
        # self.index = index

    def similarities(self):
        file = open(self.e_star_set, 'r')
        G = nx.read_adjlist(self.e_star_set)
        file.close()

        shortest_paths = nx.all_pairs_shortest_path_length(G)

        #Common Neighbors
        for node in G.nodes:
            node_neighbors = G.neighbors(node)
            for node_neighbor in node_neighbors:
                if node != node_neighbor:
                    common_neighbors = nx.common_neighbors(G, node, node_neighbor)
                    for el1 in list(common_neighbors):
                        print(el1)

        #common_neighbors = nx.cn_soundarajan_hopcroft(G)
        jaccard_coefficient = nx.jaccard_coefficient(G)
        adamic_adar = nx.adamic_adar_index(G)
        preferential_attachment = nx.preferential_attachment(G)

        for el in list(shortest_paths):
            print(el)






