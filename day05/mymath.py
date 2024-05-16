def add(x, y):
    return x + y

# I know there is a bug here!
def area(width, height):
    return width + height


def fibonacci(n):
    """
    calculate the fibonacci series

    return the Fibonacci number
    >>> fibonacci(3)
    2
    >>> fibonacci(5)
    5
    """
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
