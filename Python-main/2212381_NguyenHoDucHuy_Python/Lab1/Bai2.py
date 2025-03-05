#Tính tổng n số nguyên tố đầu tiên
def sum_first_n_integers(n):
    """Tính tổng n số nguyên đầu tiên"""
    if n == 1:
        return 1
    else:
        return n + sum_first_n_integers(n - 1)

#Tính giai thừa của n(n!)
def factorial(n):
    """Tính n!"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#Kiểm tra 1 số nguyên tố có phải là sô Fibonacci hay không
def is_fibonacci(n, a=0, b=1):
    """Kiểm tra số n có phải là số Fibonacci hay không"""
    if n == a or n == b:
        return True
    elif b > n:
        return False
    else:
        return is_fibonacci(n, b, a + b)

#Tìm số Fibonacci thứ n
def fibonacci(n):
    """Tìm số Fibonacci thứ n"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Tính tổng n số Fibonacci đầu tiên
def sum_first_n_fibonacci(n):
    """Tính tổng n số Fibonacci đầu tiên"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + sum_first_n_fibonacci(n - 1)

#Tính tổng căn bậc 2 của n số nguyên đầu tiên
import math

def sum_sqrt_first_n_integers(n):
    """Tính tổng căn bậc 2 của n số nguyên đầu tiên"""
    if n == 1:
        return math.sqrt(1)
    else:
        return math.sqrt(n) + sum_sqrt_first_n_integers(n - 1)
