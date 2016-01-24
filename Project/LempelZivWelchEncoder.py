class LempelZivWelchEncoder(object):

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
        if self.input is None:
            raise ValueError("Input is not set!")
        if self.input in self.memory:
            return self.memory[self.input]
        dict_size = 256
        dictionary = {chr(i): chr(i) for i in range(dict_size)}

        w = ""
        result = []
        for c in self.input:
            wc = w + c
            if wc in dictionary:
                w = wc
            else:
                result.append(dictionary[w])
                dictionary[wc] = dict_size
                dict_size += 1
                w = c

        if w:
            result.append(dictionary[w])
        self.memory[self.input] = result
        return result
