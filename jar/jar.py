class Jar:
    def __init__(self, capacity=12):

        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.n = n

        if self.n > self.capacity or self.n < 0:
            raise ValueError
        return self.size + self.n



    def withdraw(self, n):
        self.n = n
        if self.n > self.capacity or self.n < 0:
            raise ValueError
        return self.capacity - self.n







    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size

