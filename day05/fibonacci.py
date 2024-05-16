import sys

from mymath import add, fibonacci, non_rcursive_fibonacci

# Not recommended to import with *
# from mymath import *
# from yourmath import *


def main():
    # if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
    #     exit(f"Usage: {sys.argv[0]} NUMBER for factorial...")

    # n = int(sys.argv[1])
    fibonacci()

    n = 3
    result = fibonacci(n)
    print(f"{n} {result}")

    n = 7
    result = fibonacci(n)
    print(f"{n} {result}")

    print(add(2, 3))
    print(add(7, -3))

    result = non_rcursive_fibonacci(n)
    print(f"{n} {result}")



main()
