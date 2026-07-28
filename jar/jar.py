class Jar:
    def __init__(self, capacity=12):

        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):

        if (self.size + n) > self.capacity or n < 0:
            raise ValueError("Too Many Cookies!")
        self.size += self.n

    def withdraw(self, n):
        if n > self.size or n < 0:
            raise ValueError

        self.size -= self.n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

