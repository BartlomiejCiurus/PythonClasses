class Time:
    def __init__(self, s=0):
        self.s = int(s)

    def __str__(self):
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec -= m * 60
        return "%s:%s:%s" % (str(h).zfill(2), str(m).zfill(2), str(sec).zfill(2))

    def __repr__(self):
        return "Time(%s)" % self.s

    def __add__(self, other):
        return Time(self.s + other.s)

    # no longer available in Python 3.0
    # def __cmp__(self, other):
    #     return cmp(self.s, other.s)

    def __int__(self):
        return self.s
