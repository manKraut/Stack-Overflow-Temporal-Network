import networkx as nx
import os
import shutil
import csv


class EStarSet:
    def __init__(self, head, graph_index, v_star_file, target_path):
        self.v_star_file = v_star_file
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
        G = nx.read_adjlist(current_dir + '/AdjacencyLists/Graph_' + str(self.graph_index) + '.adjlist')

        for node in nodelist_vstar:
            valid_node_list = []                # create list to store edges that happened in given Graph
            Gadj_node_list = G.neighbors(node)  # neighbours of node in given nodelist
            for nd in Gadj_node_list:           # check if neighbour of node is in the nodelist
                if nd in nodelist_vstar:
                    valid_node_list.append(nd)  # then append it to the edges_list
            e_star.update({node: valid_node_list})

        w = csv.writer(open('E_Star_G_' + str(self.graph_index) + '.csv', 'w'))
        for key, values in e_star.items():
            w.writerow([key, values])
        shutil.move('E_Star_G' + str(self.graph_index) + '.csv', self.target_path)

