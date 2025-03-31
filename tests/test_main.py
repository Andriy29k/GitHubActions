import myApp

from myApp.main import add, substraction, multiply, divide, power, equal

def test_add():
    assert add(11, 3) == 14


def test_substraction():
    assert substraction(13, 3) == 10


def test_multiply():
    assert multiply(5, 5) == 25


def test_divide():
    assert divide(3, 0) == ZeroDivisionError
    assert divide(35, 7) == 5


def test_power():
    assert power(20, 0) == 1
    assert power(3, 3) == 27


def equal():
    assert equal(2, 5) == "Not equal"
    assert equal(1, 1) == "Equal"
