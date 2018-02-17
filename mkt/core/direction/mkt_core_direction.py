class Direction(object):

    def __init__(self, start=5):
        if start == 5:
            self.__s, self.__f = 5,3
        elif start == 3:
            self.__s, self.__f = 3,5
        else:
            self.__s, self.__f = 5,3

    @property
    def start(self):
        return self.__s

    @start.setter
    def start(self, value):
        if value == 5:
            self.__s, self.__f = 5,3
        elif value == 3:
            self.__s, self.__f = 3,5
        else:
            self.__s, self.__f = 5,3

    @property
    def finish(self):
        return self.__f

    def complementary(self):
        self.__s, self.__f = self.__f, self.__s

    def __eq__(self, other):
        return self.start == other.start

    def __repr__(self):
        return "{}'->{}'".format(self.__s, self.__f)
