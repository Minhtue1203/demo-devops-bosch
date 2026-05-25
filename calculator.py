def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    if n < 0:
        raise ValueError("Negative number not allowed")

    if n == 0:
        return 1

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result
