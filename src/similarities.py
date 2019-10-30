import networkx as nx
import csv
from collections import Counter

class Similarities:
    def __init__(self, e_star_set, e_star_set_next, pdg, pcn, pjc, pa, ppa):
        self.e_star_set = e_star_set
        self.e_star_set_next = e_star_set_next
        self.pdg = pdg
        self.pcn = pcn
        self.pjc = pjc
        self.pa = pa
        self.ppa = ppa
        # self.index = index

    def similarities(self):
        #Load files to variables
        file = open(self.e_star_set, 'r')
        file_next = open(self.e_star_set_next, 'r')
        G = nx.read_adjlist(self.e_star_set)
        G_next = nx.read_adjlist(self.e_star_set_next)
        file.close()
        file_next.close()

        ################## Shortest Path #########################
        shortest_paths = nx.all_pairs_shortest_path_length(G)
        flat_shortest_paths = {}
        for pairValue in shortest_paths:
            for (key, value) in pairValue[1].items():
                flat_shortest_paths.update({pairValue[0] + "," + key: value})

        itemsShortestsPathCount = int(len(flat_shortest_paths) * (self.pdg * 0.01))
        k1 = Counter(flat_shortest_paths)
        TopShortestsPathOfPDG = k1.most_common(itemsShortestsPathCount)
        PairsInBothStarSets = 0
        for pairValue in TopShortestsPathOfPDG:
            isEdgeExists = G_next.has_edge(pairValue[0].split(',')[0], pairValue[0].split(',')[1])
            if isEdgeExists:
                PairsInBothStarSets += 1

        print("Percentage of success for PDG is " + str((PairsInBothStarSets / itemsShortestsPathCount) * 100))


        ############ Common Neighbors #########################
        total_neighbors = {}
        for node in G.nodes:
            node_neighbors = G.neighbors(node)
            for node_neighbor in node_neighbors:
                common_neighbors = nx.common_neighbors(G, node, node_neighbor)
                total_neighbors.update({node + "," + node_neighbor: len(list(common_neighbors))})

        totalNumberofNeighbors = int(len(total_neighbors) * (self.pcn * 0.01))
        k = Counter(total_neighbors)
        # Finding N highest values
        TopPairValuesOfPCN = k.most_common(totalNumberofNeighbors)
        PairsInBothStarSets = 0
        for pairValue in TopPairValuesOfPCN:
            isEdgeExists = G_next.has_edge(pairValue[0].split(',')[0], pairValue[0].split(',')[1])
            if isEdgeExists:
                PairsInBothStarSets += 1

        print("Percentage of success for PCN is " + str((PairsInBothStarSets/totalNumberofNeighbors)*100))

        ############# Jaccard Coefficient#########################
        jaccard_coefficient = nx.jaccard_coefficient(G)
        flat_jaccard_coefficient = {}
        for pairValue in jaccard_coefficient:
                flat_shortest_paths.update({pairValue[0] + "," + pairValue[1]: pairValue[2]})

        totaljaccard_coefficientCount = int(len(flat_shortest_paths) * (self.pjc * 0.01))
        k = Counter(flat_shortest_paths)
        TopPairValuesOfPJC = k.most_common(totaljaccard_coefficientCount)
        PairsInBothStarSets = 0
        for pairValue in TopPairValuesOfPJC:
            isEdgeExists = G_next.has_edge(pairValue[0].split(',')[0], pairValue[0].split(',')[1])
            if isEdgeExists:
                PairsInBothStarSets += 1

        print("Percentage of success for PJC is " + str((PairsInBothStarSets / totaljaccard_coefficientCount) * 100))

        ############# Adamic adar index#########################
        adamic_adar = nx.adamic_adar_index(G)
        flat_adamic_adar = {}
        for pairValue in adamic_adar:
            flat_adamic_adar.update({pairValue[0] + "," + pairValue[1]: pairValue[2]})

        total_adamic_adarCount = int(len(flat_adamic_adar) * (self.pa * 0.01))
        k = Counter(flat_adamic_adar)
        TopPairValuesOfPA = k.most_common(total_adamic_adarCount)
        PairsInBothStarSets = 0
        for pairValue in TopPairValuesOfPA:
            isEdgeExists = G_next.has_edge(pairValue[0].split(',')[0], pairValue[0].split(',')[1])
            if isEdgeExists:
                PairsInBothStarSets += 1

        print("Percentage of success for PA is " + str((PairsInBothStarSets / total_adamic_adarCount) * 100))


        ############# Preferential Attachment #########################
        preferential_attachment = nx.preferential_attachment(G)
        flat_preferential_attachment = {}
        for pairValue in preferential_attachment:
            flat_preferential_attachment.update({pairValue[0] + "," + pairValue[1]: pairValue[2]})

        total_preferential_attachmentCount = int(len(flat_preferential_attachment) * (self.ppa * 0.01))
        k = Counter(flat_preferential_attachment)
        TopPairValuesOfPPA = k.most_common(total_preferential_attachmentCount)
        PairsInBothStarSets = 0
        for pairValue in TopPairValuesOfPPA:
            isEdgeExists = G_next.has_edge(pairValue[0].split(',')[0], pairValue[0].split(',')[1])
            if isEdgeExists:
                PairsInBothStarSets += 1

        print("Percentage of success for PPA is " + str((PairsInBothStarSets / total_preferential_attachmentCount) * 100))







