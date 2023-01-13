class Heap:
    values = []
    size = 0

    def __int__(self):
        self.values = []
        self.size = 0

    def string(self):
        print(self.values)
        return " ".join(self.values)

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
            pos = (pos - 1) // 2

    def extract_min(self):
        if not self.size:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.lift_down(0)
        return tmp

    def lift_down(self, i):
        while 2 * i + 1 < self.size:
            j = i
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:
                j = 2 * i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]


test = Heap()
test.insert(8)
test.insert(3)
test.insert(8)
test.insert(4)
test.insert(6)
print(test.string())
