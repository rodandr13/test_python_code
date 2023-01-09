class Heap:

    def __int__(self):
        self.values = []
        self.size = 0

    def insert(self, value):
        self.values.append(value)
        self.size += 1
        self.lift_up(self.size - 1)

    def lift_up(self, pos):
        while (
                pos != 0 and
                self.values[pos] < self.values[(pos - 1) // 2]
        ):
            self.values[pos] = self.values[(pos - 1) // 2]
            self.values[(pos - 1) // 2] = self.values[pos]
