def factorial(n):
    fact = 1

    for i in range (1, n + 1):
        fact = fact * i

    return fact

def approx_sin(x, n):
    total = 0

    for i in range(n):
        total = total + ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)

    return total


def approx_cos(x, n):
    total = 0

    for i in range(n):
        total = total + ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    
    return total


def approx_sinh(x, n):
    total = 0

    for i in range(n):
        total = total + (x ** (2 * i + 1)) / factorial(2 * i + 1)
    
    return total


def approx_cosh(x, n):
    total = 0

    for i in range(n):
        total = total + (x ** (2 * i)) / factorial(2 * i)
    
    return total

print(approx_sin(x=3.14, n=10))
print(approx_cos(x=3.14, n=10))
print(approx_sinh(x=3.14, n=10))
print(approx_cosh(x=3.14, n=10))