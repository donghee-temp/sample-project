def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n-1)
