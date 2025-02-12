#1.Hàm thực hiện các phép tính
def perform_operations(a, b):

    sum_result = a + b
    
    if b != 0:
        division_result = a / b
    else:
        division_result = "Không thể chia cho 0"
    
    
    power_result = a ** b
    
    return sum_result, division_result, power_result

a = 5
b = 2

sum_result, division_result, power_result = perform_operations(a, b)


print(f"a + b = {sum_result}")
print(f"a / b = {division_result}")
print(f"a^b = {power_result}")

#2.Tính diện tích hình chữ nhật khi biết bán kinh đường tròn
#Bán kính đường tròn nội tiếp hình chữ nhật
import math

def dien_tich_noi_tiep(r, l):
    w = 2 * r
    dien_tich = l * w
    return dien_tich

ban_kinh = 5
chieu_dai = 12
dien_tich = dien_tich_noi_tiep(ban_kinh, chieu_dai)
print("Diện tích hình chữ nhật:", dien_tich)

#Bán kính đường tròn ngoại tiếp hình chữ nhật
def dien_tich_ngoai_tiep(r, l):
    duong_cheo = 2 * r
    w = math.sqrt(duong_cheo**2 - l**2)
    dien_tich = l * w
    return dien_tich

ban_kinh = 5
chieu_dai = 8
dien_tich = dien_tich_ngoai_tiep(ban_kinh, chieu_dai)
print("Diện tích hình chữ nhật:", dien_tich)

#3.Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
def is_prime(n):
    """Kiểm tra một số có phải là số nguyên tố không."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Trả về danh sách các số nguyên tố trong khoảng [start, end]."""
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes

start = 10
end = 50
print(f"Các số nguyên tố trong khoảng từ {start} đến {end} là:")
print(primes_in_range(start, end))

#4.Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
import math

def is_perfect_square(x):
    """Kiểm tra một số có phải là số chính phương không."""
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    """Kiểm tra xem một số có phải là số Fibonacci không."""
    if n < 0:
        return False
    # Kiểm tra điều kiện của số Fibonacci
    return is_perfect_square(5 * n**2 + 4) or is_perfect_square(5 * n**2 - 4)

n = int(input("Nhập một số nguyên: "))
if is_fibonacci(n):
    print(f"{n} là một số Fibonacci.")
else:
    print(f"{n} không phải là số Fibonacci.")

#5.Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
#Cách dùng đệ quy
def fibonacci_recursive(n):
    """Tìm số Fibonacci thứ n bằng đệ quy."""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Ví dụ
n = int(input("Nhập số nguyên n: "))
print(f"Số Fibonacci thứ {n} (đệ quy) là: {fibonacci_recursive(n)}")
#Cách dùng vòng lặp(Không dùng đệ quy)
def fibonacci_iterative(n):
    """Tìm số Fibonacci thứ n bằng vòng lặp."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Ví dụ
n = int(input("Nhập số nguyên n: "))
print(f"Số Fibonacci thứ {n} (vòng lặp) là: {fibonacci_iterative(n)}")

#6.Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)
#Cách dùng đệ quy
def fibonacci_recursive(n):
    """Tính số Fibonacci thứ n."""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def sum_fibonacci_recursive(n):
    """Tính tổng n số Fibonacci đầu tiên bằng đệ quy."""
    if n == 0:
        return 0
    return fibonacci_recursive(n-1) + sum_fibonacci_recursive(n-1)

n = int(input("Nhập n: "))
print(f"Tổng {n} số Fibonacci đầu tiên (đệ quy) là: {sum_fibonacci_recursive(n)}")

#Cách không dùng đệ quy(dùng vòng lặp)
def sum_fibonacci_iterative(n):
    """Tính tổng n số Fibonacci đầu tiên bằng vòng lặp."""
    if n == 0:
        return 0
    a, b = 0, 1
    sum_fib = a + b
    for _ in range(2, n):
        a, b = b, a + b
        sum_fib += b
    return sum_fib if n > 1 else a

n = int(input("Nhập n: "))
print(f"Tổng {n} số Fibonacci đầu tiên (vòng lặp) là: {sum_fibonacci_iterative(n)}")

#7.Tính tổng căn bậc 2 của n số nguyên đầu tiên
import math

def sum_square_roots_pythonic(n):
    """Tính tổng căn bậc 2 của n số nguyên đầu tiên bằng list comprehension."""
    return sum([math.sqrt(i) for i in range(1, n + 1)])

# Ví dụ
n = int(input("Nhập n: "))
print(f"Tổng căn bậc 2 của {n} số nguyên đầu tiên (Pythonic) là: {sum_square_roots_pythonic(n)}")

#8.Giải phương trình bậc 2: ax2 + bx + c=0
import math

def giai_phuong_trinh_bac_2(a, b, c):
    """Giải phương trình bậc 2: ax^2 + bx + c = 0"""
    # Kiểm tra a có bằng 0 không
    if a == 0:
        if b == 0:
            return "Phương trình vô nghiệm." if c != 0 else "Phương trình có vô số nghiệm."
        else:
            return f"Nghiệm duy nhất: x = {-c/b:.2f}"
    
    # Tính delta
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Hai nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif delta == 0:
        x = -b / (2*a)
        return f"Nghiệm kép: x = {x:.2f}"
    else:
        return "Phương trình vô nghiệm thực."

# Nhập hệ số từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Gọi hàm và in kết quả
print(giai_phuong_trinh_bac_2(a, b, c))

#9.Tính n!
import math

n = int(input("Nhập số nguyên n: "))
print(f"{n}! = {math.factorial(n)}")
5