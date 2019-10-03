class VStarSets:
    def __init__(self, N):
        self.N = N

    def v_star_set(self):
        i = 1
        nodelist1 = []
        nodelist2 = []
        while True:
            if i <= self.N:
                with open('Graph_nodes_' + str(i) + '.txt', 'r') as graph1:
                    for line in graph1:
                        nodelist1.append(int(line.strip()))
                with open('Graph_nodes_' + str(i+1) + '.txt', 'r') as graph2:
                    for line in graph2:
                        nodelist2.append(int(line.strip()))

                v_star_set = set(nodelist1) & set(nodelist2)
                with open('V_Star_G_' + str(i) + "_" + str(i+1) + '.txt', 'w') as fp:
                    for n in v_star_set:
                        fp.write(str(n) + "\n")
                i += 2
            else:
                break
