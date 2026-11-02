from jar import Jar
import pytest


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


# def test_functionName():
# Write test codet
# assert function(input)==return
def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "\U0001F36A\U0001F36A\U0001F36A\U0001F36A\U0001F36A"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(8)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)

if __name__ == "__main__":
    main()
