class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError
        else:
            self._capacity=capacity
            self._size=0

    def __str__(self):
        return"🍪"*self.size

    def deposit(self, n):
        if self.capacity-n<0:
            raise ValueError
        self.capacity-=n
        self.size+=n

    def withdraw(self, n):
        if self.size-n<0:
            raise ValueError
        self.capacity+=n
        self.size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError
        self._capacity = value

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError
        self._size = value


def main():
    jar=Jar()
    jar.deposit(3)
    print(jar)
if __name__=="__main__":
        main()