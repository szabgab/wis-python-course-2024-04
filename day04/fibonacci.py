import sys

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
        exit(f"Usage: {sys.argv[0]} NUMBER for factorial...")

    n = int(sys.argv[1])

    result = fibonacci(n)
    print(f"{n} {result}")

    result = non_rcursive_fibonacci(n)
    print(f"{n} {result}")

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def non_rcursive_fibonacci(n):
    if n == 1:
        [1]
    if n == 2:
        [1, 1]

    result = [1, 1]

    for _ in range(2, n):
        # result.append(result[len(result)-1] + result[len(result)-2])
        result.append(result[-1] + result[-2])
    
    return result

main()
