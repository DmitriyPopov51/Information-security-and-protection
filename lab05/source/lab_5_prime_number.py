print("-----------------------------------------------------")
print(" Вероятностные алгоритмы проверки чисел на простоту")
print("-----------------------------------------------------")


import random


def ferma(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def jacobi(n, a):
    if n % 2 == 0 or n <= 0:
        raise ValueError("условие n >= 3 и n нечетное - не выполнено")
    a = a % n
    g = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                g = -g
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            g = -g
        a = a % n
    if n == 1:
        return g
    else:
        return 0


def strassen(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        r = pow(a, (n - 1) // 2, n)
        s = jacobi(n=n, a=a)
        if r != s % n:
            return False
    return True


def miller_rabin(n, k=10):
    def miller_rabin_test(a, s, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False
    if n <= 1:
        return False
    if n <= 3:
        return True
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_rabin_test(a, s, d, n):
            return False
    return True



print("Тест Ферма: ")
n = 119
if ferma(n):
    print(f"Число {n}, вероятно, простое")
else:
    print(f"Число {n} составное")
print()
n1 = 2
n2 = 15
symbol = jacobi(n=n2, a=n1)
print(f"Символ Якоби ({n1}/{n2}) = {symbol}")
print()
print("Тест Соловэя-Штрассена: ")
if strassen(n):
    print(f"Число {n}, вероятно, простое")
else:
    print(f"Число {n} составное")
print()
print("Тест Миллера-Рабина: ")
if miller_rabin(n):
    print(f"Число {n}, вероятно, простое")
else:
    print(f"Число {n} составное")