from io import StringIO


class LempelZivWelchDecoder(object):

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

        dict_size = 256
        dictionary = {chr(i): chr(i) for i in range(dict_size)}

        result = StringIO()
        w = self.input.pop(0)
        result.write(w)
        for k in self.input:
            if k in dictionary:
                entry = dictionary[k]
            elif k == dict_size:
                entry = w + w[0]
            else:
                raise ValueError('Bad compression of k: ' + k)
            result.write(entry)

            dictionary[dict_size] = w + entry[0]
            dict_size += 1

            w = entry

        return result.getvalue()
