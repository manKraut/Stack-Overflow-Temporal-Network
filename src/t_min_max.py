class TValues:
    def __init__(self, head):
        self.head = head

    def get_absolute_t_values(self):
        t_values = []
        for field in self.head:
            t = field.split()
            t_values.append(int(t[-1]))
        return t_values

    def get_relative_t_values(self):
        t_values = self.get_absolute_t_values()
        diff = t_values[0]
        relative_t_values = [x - diff for x in t_values]
        return relative_t_values


class MinMax:
    def __init__(self, head):
        self.head = head

    def min_max(self):
        values = TValues(self.head).get_absolute_t_values()
        minimum = values[0]
        maximum = values[-1]
        print("The minimum value of time found in provided set is: " + str(minimum) + "\n")
        print("The maximum value of time found in provided set is: " + str(maximum) + "\n")
        return minimum, maximum

