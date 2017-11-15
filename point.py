class Point(object):

    square = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_square(self):
        return self.square

    def set_square(self, square):
        self.square = square

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
