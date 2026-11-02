
def main():
    my_jar = Jar()

    print(my_jar)


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capasity can not be less then 0")
        else:
            self._capacity = capacity
            self._size = 0


    def __str__(self):
        cookie = "\U0001F36A"
        return_value = ""
        i = 0
        while i <= (self._size - 1):
            return_value = f"{return_value}{cookie}"
            i += 1
        return return_value

    def deposit(self, n):
        if (self._size + n) > self._capacity:
            raise ValueError("Amount is highet then jars capasity")
        else:
            self._size = self._size + n

    def withdraw(self, n):
        if (self._size - n) < 0:
            raise ValueError("Noth enough cookies in the jar")
        else:
            self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


if __name__ == "__main__":
    main()
