class Label:

    def __init__(self, value, group):
        self.value = value
        self.group = group

    def __eq__(self, other):
        return self.value == other.value and self.group == other.group



