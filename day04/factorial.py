import sys

def main():
    # print(sys.argv)
    # print(len(sys.argv))

    # if len(sys.argv) != 2:
    #     exit(f"Usage: {sys.argv[0]} NUMBER for factorial...")

    # if not sys.argv[1].isnumeric():
    #     exit(f"Usage: {sys.argv[0]} NUMBER for factorial...")

    if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
        exit(f"Usage: {sys.argv[0]} NUMBER for factorial...")

    n = int(sys.argv[1])

    # It is a very bad idea to hard-code pathes and file-names in a program
    # file = "c:\\users\\Foo Bar\\reasearch\\blue.xls"

    # n = int(input("type in a number: "))

    result = factorial(n)
    print(f"{n} {result}")

    result = non_rcursive_factorial(n)
    print(f"{n} {result}")

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

def non_rcursive_factorial(n):
    result = 1
    for i in range(1, n+1):
        result = i * result
    
    return result

main()
