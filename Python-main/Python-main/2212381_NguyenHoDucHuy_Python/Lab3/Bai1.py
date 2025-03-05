numbers = [3, 5, 8, 10, 15, 20, 22, 7, 9, 12]
odd_numbers_not_divisible_by_5 = [num for num in numbers if num % 2 != 0 and num % 5 != 0]

# Xuất các số lẻ không chia hết cho 5
print("Các số lẻ không chia hết cho 5:")
print(odd_numbers_not_divisible_by_5)

# Hàm kiểm tra số Fibonacci
def is_fibonacci(n):
    """Kiểm tra số Fibonacci"""
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Tìm các số Fibonacci trong list
fibonacci_numbers = [num for num in numbers if is_fibonacci(num)]

# Xuất các số Fibonacci
print("Các số Fibonacci trong list:")
print(fibonacci_numbers)

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    """Kiểm tra số nguyên tố"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tìm các số nguyên tố trong list
prime_numbers = [num for num in numbers if is_prime(num)]

# Tìm số nguyên tố lớn nhất
if prime_numbers:
    max_prime = max(prime_numbers)
else:
    max_prime = None

# Xuất số nguyên tố lớn nhất
print("Số nguyên tố lớn nhất trong list:")
print(max_prime)

# Hàm kiểm tra số Fibonacci
def is_fibonacci(n):
    """Kiểm tra số Fibonacci"""
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Tìm các số Fibonacci trong list
fibonacci_numbers = [num for num in numbers if is_fibonacci(num)]

# Tìm số Fibonacci bé nhất
if fibonacci_numbers:
    min_fibonacci = min(fibonacci_numbers)
else:
    min_fibonacci = None

# Xuất số Fibonacci bé nhất
print("Số Fibonacci bé nhất trong list:")
print(min_fibonacci)