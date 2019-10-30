import networkx as nx
import os
import shutil
import csv


class EStarSet:
    def __init__(self, head, graph_index, v_star_file, v_star_index, target_path):
        self.v_star_file = v_star_file
        self.v_star_index = v_star_index
        self.graph_index = graph_index
        self.head = head
        self.target_path = target_path

    def e_star(self):
        e_star = {}
        nodelist_vstar = []
        with open(self.v_star_file, 'r') as vf:
            for line in vf:
                nodelist_vstar.append(int(line.strip()))

        current_dir = os.getcwd()
        G = nx.read_adjlist(current_dir + '/AdjacencyLists/Graph_' + str(self.graph_index) + '.adjlist', nodetype=int)

        for node in nodelist_vstar:
            valid_node_list = []                # create list to store edges that happened in given Graph
            if node in G.node():
                Gadj_node_list = G.neighbors(node)  # neighbours of node in given nodelist
                for nd in Gadj_node_list:           # check if neighbour of node is in the nodelist
                    if nd in nodelist_vstar:
                        valid_node_list.append(nd)  # then append it to the edges_list
            if len(valid_node_list) != 0:
                e_star.update({node: valid_node_list})

        e_star_graph = nx.from_dict_of_lists(e_star)
        nx.write_adjlist(e_star_graph, 'E_Star_G_' + str(self.v_star_index) + '_' + str(self.graph_index) + '.adjlist')

        # with open('E_Star_G_' + str(self.v_star_index) + '_' + str(self.graph_index) + '.txt', 'w') as file:
        #     w = csv.writer(file)
        #     for key, values in e_star.items():
        #         w.writerow([key, values])
        shutil.move('E_Star_G_' + str(self.v_star_index) + '_' + str(self.graph_index) + '.adjlist', self.target_path)
