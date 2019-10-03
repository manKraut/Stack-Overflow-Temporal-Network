import t_min_max
import csv


class Partition:
    def __init__(self, head, t_min, t_max):
        self.head = head
        self.t_min = t_min
        self.t_max = t_max
        self.t_values = []

    def partition(self):
        print("Please, enter the factor N, by which the corresponding time span will be divided")
        Dt = self.t_max - self.t_min
        N = int(input())
        dt = Dt / N
        print(dt)
        T = {}
        j = 0
        flag = 0
        self.t_values = t_min_max.TValues(self.head).get_relative_t_values()
        for i in range(1, N + 1):
            tj = []
            if flag != 0:
                tj.append(flag)
            for item in self.t_values[j:]:
                if item <= i * dt:
                    tj.append(item)
                    j += 1
                else:
                    if tj[-1] != i * dt:
                        tj.append(i * dt)
                        flag = i * dt
                    break
            T[i] = tj
            # w = csv.writer(open("timestamps_graph_" + str(i) + ".csv", "w"))
            # w.writerow(tj)
        print(T)
        return T, N
