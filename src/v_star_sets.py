import os
import shutil


class VStarSets:
    def __init__(self, N, target_path):
        self.N = N
        self.target_path = target_path

    def v_star_set(self):
        i = 0
        nodelist1 = []
        nodelist2 = []
        current_dir = os.getcwd()
        while True:
            if i <= (self.N-2):
                with open(os.path.join(current_dir, 'Graphs/Graph_nodes_' + str(i) + '.txt'), 'r') as graph1:
                    for line in graph1:
                        nodelist1.append(int(line.strip()))
                with open(os.path.join(current_dir, 'Graphs/Graph_nodes_' + str(i+1) + '.txt'), 'r') as graph2:
                    for line in graph2:
                        nodelist2.append(int(line.strip()))

                v_star_set = [value for value in nodelist1 if value in nodelist2]
                with open('V_Star_G_' + str(i) + "_" + str(i+1) + '.txt', 'w') as fp:
                    for n in v_star_set:
                        fp.write(str(n) + "\n")
                shutil.move('V_Star_G_' + str(i) + "_" + str(i+1) + '.txt', self.target_path)
                i += 1
            else:
                break
