class RunLengthDecoder(object):

    def __init__(self):
        self._input = None

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        self._input = value

    def decode(self):
        if self.input is None:
            raise ValueError("Input is not set!")
        decoded = ""
        for character, count in self.input:
            decoded += character * count
        return decoded
