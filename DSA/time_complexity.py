def test(n: list[int, str]):
    """ O(1) """
    print("test")


def test1(n: list[int, str]):
    """ O(n) """
    for i in n:
        print("test")


def test2(n: list[int]):
    """ O(n) """
    for i in n:
        print("hi")
    for i in n:
        print("hi")


def test3(n: list[int]):
    """ O(n**2) """
    for i in n:
        print("hi")
        for j in n:
            print("hi")


def test4(n: list[int]):
    for i in n:
        for j in n:
            if (i + j) == 9:
                print("9 found")
