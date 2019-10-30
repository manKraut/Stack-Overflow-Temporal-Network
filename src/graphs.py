import networkx as nx
import csv
import matplotlib.pyplot as plt
import shutil
import os

import t_min_max


class GraphAtts:
    def __init__(self, T, head, graphs_target_path, adjacency_target_path):
        self.T = T
        self.head = head
        self.t_values = []
        self.graphs_target_path = graphs_target_path
        self.adjacency_target_path = adjacency_target_path

    def adjacency_matrix(self):
        temp = 0
        name = 0
        self.t_values = t_min_max.TValues(self.head).get_relative_t_values()
        for j in self.T.values():
            g = nx.DiGraph(name='set ' + str(name))
            for value in j:
                for z in self.t_values[temp:]:
                    if value == z:
                        node_list = []
                        node_1 = int(self.head[temp].split()[0])
                        node_2 = int(self.head[temp].split()[1])
                        node_list.append(node_1)
                        node_list.append(node_2)
                        g.add_node(node_1)
                        g.add_node(node_2)
                        g.add_edge(node_1, node_2)
                        temp += 1
                        break
            print(nx.info(g))
            # write list of nodes that belong to each graph, into txt file for further manipulation
            graph_node_list = list(g.nodes)
            with open('Graph_nodes_' + str(name) + '.txt', 'w') as fp:
                for n in graph_node_list:
                    fp.write(str(n) + "\n")

            # write graph into txt file for easy retrieval when it's necessary
            nx.write_adjlist(g, "Graph_" + str(name) + ".adjlist")

            shutil.move('Graph_nodes_' + str(name) + '.txt', self.graphs_target_path)
            shutil.move('Graph_' + str(name) + '.adjlist', self.adjacency_target_path)
            print('End of matrix' + str(name) + '\n')

            nx.draw(g)
            nx.draw(g, with_labels=False)
            plt.savefig('Graph' + str(name) + '.png', format="PNG")
            shutil.move('Graph' + str(name) + '.png', self.graphs_target_path)
            # plt.show()

            name += 1

class GraphToCsv:
    def __init__(self, name, adjacency_target_path):
        self.name = name
        self.adjacency_target_path = adjacency_target_path

    def centralities_to_csv(self):
        G = nx.read_adjlist(os.path.join(self.adjacency_target_path, "graph_" + str(self.name) + ".adjlist"))
        dcntr = nx.degree_centrality(G)
        ccntr = nx.closeness_centrality(G)
        bcntr = nx.betweenness_centrality(G)
        ecntr = nx.eigenvector_centrality(G, 1000)
        kcntr = nx.katz_centrality(G)

        w = csv.writer(open("degree_centrality_graph_" + str(self.name) + ".csv", "w"))
        for key, val in dcntr.items():
            w.writerow([key, val])

        w = csv.writer(open("closeness_centrality_graph_" + str(self.name) + ".csv", "w"))
        for key, val in ccntr.items():
            w.writerow([key, val])

        w = csv.writer(open("betweenness_centrality_graph_" + str(self.name) + ".csv", "w"))
        for key, val in bcntr.items():
            w.writerow([key, val])

        w = csv.writer(open("eigenvector_centrality_graph_" + str(self.name) + ".csv", "w"))
        for key, val in ecntr.items():
            w.writerow([key, val])

        w = csv.writer(open("katz_centrality_graph_" + str(self.name) + ".csv", "w"))
        for key, val in kcntr.items():
            w.writerow([key, val])

        return dcntr, ccntr, bcntr, ecntr, kcntr


class Diagrams:
    def __init__(self, dcntr, ccntr, bcntr, ecntr, kcntr, graph_index, current_path):

        self.dcntr = dcntr
        self.ccntr = ccntr
        self.bcntr = bcntr
        self.ecntr = ecntr
        self.kcntr = kcntr
        self.graph_index = graph_index
        self.current_path = current_path

    def centralities_diagrams(self):
        # sort degree centrality dictionaries by value
        sorted_dcntr = sorted(self.dcntr.items(), key=lambda kv: kv[1])
        sorted_dcntr = dict(sorted_dcntr)

        dcntr_values_key = [sorted_dcntr[next(iter(sorted_dcntr))]]
        counter = 0
        dcntr_nodes_value = []
        for item in sorted_dcntr:
            if sorted_dcntr[item] != dcntr_values_key[-1]:
                dcntr_values_key.append(sorted_dcntr[item])
                dcntr_nodes_value.append(counter/len(sorted_dcntr))
                counter = 1
            else:
                counter += 1
        dcntr_nodes_value.append(counter/len(sorted_dcntr))

        plt.plot(dcntr_values_key, dcntr_nodes_value)
        plt.savefig('Degree_centrality_' + str(self.graph_index) + '.png', format="PNG")
        plt.show()

        # sort closeness centrality dictionaries by value
        sorted_ccntr = sorted(self.ccntr.items(), key=lambda kv: kv[1])
        sorted_ccntr = dict(sorted_ccntr)
        ccntr_values_key = [sorted_ccntr[next(iter(sorted_ccntr))]]
        counter = 0
        ccntr_nodes_value = []

        for item in sorted_ccntr:
            if sorted_ccntr[item] != ccntr_values_key[-1]:
                ccntr_values_key.append(sorted_ccntr[item])
                ccntr_nodes_value.append(counter/len(sorted_ccntr))
                counter = 1
            else:
                counter += 1
        ccntr_nodes_value.append(counter/len(sorted_ccntr))

        plt.plot(ccntr_values_key, ccntr_nodes_value)
        plt.savefig('Closeness_centrality_' + str(self.graph_index) + '.png', format="PNG")
        plt.show()

        # sort closeness centrality dictionaries by value
        sorted_bcntr = sorted(self.bcntr.items(), key=lambda kv: kv[1])
        sorted_bcntr = dict(sorted_bcntr)
        bcntr_values_key = [sorted_bcntr[next(iter(sorted_bcntr))]]
        counter = 0
        bcntr_nodes_value = []

        for item in sorted_bcntr:
            if sorted_bcntr[item] != bcntr_values_key[-1]:
                bcntr_values_key.append(sorted_bcntr[item])
                bcntr_nodes_value.append(counter / len(sorted_bcntr))
                counter = 1
            else:
                counter += 1
        bcntr_nodes_value.append(counter / len(sorted_bcntr))

        plt.plot(bcntr_values_key, bcntr_nodes_value)
        plt.savefig('Betweenes_centrality_' + str(self.graph_index) + '.png', format="PNG")
        plt.show()

        # sort closeness centrality dictionaries by value
        sorted_ecntr = sorted(self.ecntr.items(), key=lambda kv: kv[1])
        sorted_ecntr = dict(sorted_ecntr)
        ecntr_values_key = [sorted_ecntr[next(iter(sorted_ecntr))]]
        counter = 0
        ecntr_nodes_value = []

        for item in sorted_ecntr:
            if sorted_ecntr[item] != ecntr_values_key[-1]:
                ecntr_values_key.append(sorted_ecntr[item])
                ecntr_nodes_value.append(counter / len(sorted_ecntr))
                counter = 1
            else:
                counter += 1
        ecntr_nodes_value.append(counter / len(sorted_ecntr))

        plt.plot(ecntr_values_key, ecntr_nodes_value)
        plt.savefig('Eigenvector_centrality_' + str(self.graph_index) + '.png', format="PNG")
        plt.show()

        # sort closeness centrality dictionaries by value
        sorted_kcntr = sorted(self.kcntr.items(), key=lambda kv: kv[1])
        sorted_kcntr = dict(sorted_kcntr)
        kcntr_values_key = [sorted_kcntr[next(iter(sorted_kcntr))]]
        counter = 0
        kcntr_nodes_value = []

        for item in sorted_kcntr:
            if sorted_kcntr[item] != kcntr_values_key[-1]:
                kcntr_values_key.append(sorted_kcntr[item])
                kcntr_nodes_value.append(counter / len(sorted_kcntr))
                counter = 1
            else:
                counter += 1
        kcntr_nodes_value.append(counter / len(sorted_kcntr))

        plt.plot(kcntr_values_key, kcntr_nodes_value)
        plt.savefig('Katz_centrality_' + str(self.graph_index) + '.png', format="PNG")
        plt.show()
