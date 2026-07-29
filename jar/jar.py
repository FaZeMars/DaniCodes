class Jar:
    def __init__(self, capacity=12):
        if not capacity:
            self.capacity = 12
        elif capacity < 0:
            raise ValueError
        else:
            self.capacity = capacity

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n, capacity):
        if not n:
            raise ValueError("Missing Cookies")
        elif not isinstance(n, int):
            raise ValueError("Not a cookie")
        elif n > self.capacity:
            raise ValueError("Too Many Cookies")
        elif n < 0:
            raise ValueError("Please Insert A Valid Number Of Cookies")
        elif not isinstance
        else:
            self.n = n


    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
