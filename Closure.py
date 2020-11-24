print("Welcome to Closure")
g = None


def f1(a, b):
    print("Entering f1")
    print("a = ", a)
    print("b = ", b)

    def f2(c, d):
        nonlocal a
        nonlocal b
        print("Entering f2")
        print("c = ", c)
        print("d = ", d)
        print("a = ", a)
        print("b = ", b)
        a = a + 3
        b = b + 4
        print("Leaving f2")

        def f3(e, f):
            print()

    f2(3, 4)
    print("a = ", a)
    print("b = ", b)
    global g
    g = f2
    print("Leaving f1")


f1(10, 20)

# Closure object
g(-1, -2)
g(8, 9)
