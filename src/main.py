import t_min_max
import t_partition
import similarities
import graphs
import v_star_sets
import e_star_sets
import shutil
import os


current_path = os.getcwd()
dir_paths = ['Graphs', 'AdjacencyLists', 'DegreeCentralities', 'ClosenessCentralities', 'BetweennessCentralities',
             'EigenVectorCentralities', 'KatzCentralities', 'VStarSets', 'EStarSets']
for path in dir_paths:
    try:
        shutil.rmtree(os.path.join(current_path, path))
    except OSError:
        print('Folder %s not found' % os.path.join(current_path, path))
    else:
        print('Deleting existing folders')
    os.mkdir(os.path.join(current_path, path))
#
with open("sx-stackoverflow-20k.txt") as my_file:
    head = []
    for line in my_file:
        head.append(line)
my_file.close()

# Question 1
minimum, maximum = t_min_max.MinMax(head).min_max()
#
# # Question 2
T, N = t_partition.Partition(head, minimum, maximum).partition()

# # # # Question 3
graphs.GraphAtts(T, head, os.path.join(current_path, dir_paths[0]), os.path.join(current_path, dir_paths[1]))\
    .adjacency_matrix()
#
# # Question 4
for i in range(N):
    dcntr, ccntr, bcntr, ecntr, kcntr = graphs.GraphToCsv(i, os.path.join(current_path, dir_paths[1]))\
        .centralities_to_csv()

    shutil.move(current_path + "/degree_centrality_graph_" + str(i) + ".csv", dir_paths[2])
    shutil.move(current_path + "/closeness_centrality_graph_" + str(i) + ".csv", dir_paths[3])
    shutil.move(current_path + "/betweenness_centrality_graph_" + str(i) + ".csv", dir_paths[4])
    shutil.move(current_path + "/eigenvector_centrality_graph_" + str(i) + ".csv", dir_paths[5])
    shutil.move(current_path + "/katz_centrality_graph_" + str(i) + ".csv", dir_paths[6])

    # graphical representation
    graphs.Diagrams(dcntr, ccntr, bcntr, ecntr, kcntr, i, current_path).centralities_diagrams()

# Question 5
# v_star_sets.VStarSets(N, dir_paths[7]).v_star_set()

# v_star_files = []
# for _, _, file in os.walk(os.path.join(current_path, dir_paths[7])):
#     v_star_files = file
#
# counter = 0
# j = 0
# target_path = os.path.join(current_path, dir_paths[8])
# for file in v_star_files:
#     v_star_file = os.path.join(os.path.join(current_path, dir_paths[7]), file)
#     v_star_index = j
#     for i in range(counter, counter + 2):
#         graph_index = i
#         e_star_sets.EStarSet(head, graph_index, v_star_file, v_star_index, target_path).e_star()
#     counter += 1
#     j += 1

# Question 6
# for i in range(N):
#     similarities.Similarities((os.path.join(current_path, dir_paths[8]) + '\E_Star_G_' + str(i) + '_' + str(i) +
#                                '.adjlist'), i).similarities()
