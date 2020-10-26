class MyArray:
    def __init__(self, values=[]):
        self.array = values
        self.current = 0

    def __getitem__(self, key):
        return self.array[key]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.current += 1
            return self.array[self.current - 1]
        except IndexError:
            self.current = 0
            raise StopIteration

    def __len__(self):
        return len(self.array)

    def __setitem__(self, key, value):
        try:
            self.array[key] = value
        except IndexError:
            assert key >= 0, 'key must be 0 or positive'
            self.array.extend(((key + 1) - len(self.array)) * [None])
            self.array[key] = value
