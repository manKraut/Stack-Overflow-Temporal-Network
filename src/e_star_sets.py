import networkx as nx


class EStarSet:
    def __init__(self, v_star_file, graph_index, head):
        self.v_star_file = v_star_file
        self.graph_index = graph_index
        self.head = head

    def e_star(self):
        e_star = []
        nodelist = []
        with open(self.v_star_file, 'r') as vf:
            for line in vf:
                nodelist.append(int(line.strip()))

        G = nx.read_adjlist('Graph_' + self.graph_index + '.adjlist')

        for node in nodelist:
            edges_list = [node]            # create list to store edges that happened in given Graph
            temp_list = list(G.adj[node])  # neighbours of node in given nodelist
            for nd in temp_list:           # check if neighbour of node is in the nodelist
                if nd in nodelist:
                    edges_list.append(nd)  # then append it to the edges_list
            e_star.append(edges_list)

        return e_star
