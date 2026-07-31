class Jar:
    def __init__(self, capacity=12):
        if not capacity:
            self.capacity = 12
        if not isinstance(capacity, int):
            raise ValueError("Not A Cookie")
        elif capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        if self._size == 0:
            return ""
        else:
            return "🍪" * self._size

    def deposit(self, n,):
        if not isinstance(n, int):
            raise ValueError("Not a cookie")
        elif self.size + n > self._capacity:
            raise ValueError("Too Many Cookies")
        elif n < 0:
            raise ValueError("No Negative Number Of Cookies")
        else:
            self.n = n
            self._size += self.n
            return self._size


    def withdraw(self, n):
        if not isinstance(n, int):
            raise ValueError("Not a cookie")
        elif n > self._size:
            raise ValueError("Too Many Cookies")
        elif n < 0:
            raise ValueError("No Negative Number Of Cookies")
        else:
            self.n = n
            self._size -= self.n
            return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
