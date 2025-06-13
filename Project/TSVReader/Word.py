class Word:

    def __init__(self, index, start, end, value):
        self.index = index
        self.start = start
        self.end = end
        self.value = value

    def __eq__(self, other):
        return self.index == other.index

    def __hash__(self):
        result = 7
        result = result * 17 + self.index
        result = result * 17 + hash(self.value)
        return result

