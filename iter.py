#!/c/Python36/python

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev=Reverse('hai')
#print(rev)
iter(rev)
for char in rev:
    print(char)

#print(tuple(rev))
