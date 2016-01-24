class RunLengthEncoder(object):

    def __init__(self):
        self._input = None
        self._memory = dict()

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        self._input = value

    @property
    def memory(self):
        return self._memory

    def encode(self):
        global character
        if self.input is None:
            raise ValueError("Input is not set!")
        if self.input in self.memory:
            return self.memory[self.input]
        count = 1
        prev = ''
        list = []
        for character in self.input:
            if character != prev:
                if prev:
                    entry = (prev, count)
                    list.append(entry)
                count = 1
                prev = character
            else:
                count += 1
        else:
            entry = (character, count)
            list.append(entry)
        self.memory[self.input] = list
        return list
