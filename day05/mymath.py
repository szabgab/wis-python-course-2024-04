def add(x, y):
    return x + y

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
