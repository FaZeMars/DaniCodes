class Jar:
    def __init__(self, capacity=12):
        if not capacity:
            self.capacity = 12
        elif capacity < 0:
            raise ValueError
        else:
            self.capacity = capacity

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
