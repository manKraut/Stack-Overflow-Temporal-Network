import t_min_max
import t_partition
import graphs
import v_star_sets


with open("sx-stackoverflow-100k.txt") as my_file:
    head = []
    for line in my_file:
        head.append(line)
my_file.close()

# Question 1
minimum, maximum = t_min_max.MinMax(head).min_max()

# Question 2
T, N = t_partition.Partition(head, minimum, maximum).partition()

# # Question 3
graphs.GraphAtts(T, head).adjacency_matrix()
#
# Question 4
# for i in range(N):
#     dcntr, ccntr, bcntr, ecntr, kcntr = graphs.GraphToCsv(i).centralities_to_csv()
#     # graphical representation
#     graphs.Diagrams(dcntr, ccntr, bcntr, ecntr, kcntr).centralities_diagrams()

#Question 5

v_star_sets.VStarSets(N).v_star_set()
