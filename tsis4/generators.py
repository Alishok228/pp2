# Генератор для квадратов чисел до N
def squares_generator(N):
    for i in range(N):
        yield i ** 2

# Генератор для четных чисел от 0 до n
def even_numbers_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

# Генератор для чисел, делящихся на 3 и 4 в диапазоне от 0 до n
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Генератор для квадратов чисел от a до b
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

# Генератор для чисел от n до 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Пример использования всех генераторов:
N = 5
print("Квадраты чисел до", N)
for square in squares_generator(N):
    print(square)

n = 10
print("\nЧетные числа от 0 до", n)
print(','.join(str(num) for num in even_numbers_generator(n)))

n = 20
print("\nЧисла, делящиеся на 3 и 4 от 0 до", n)
for num in divisible_by_3_and_4(n):
    print(num)

a, b = 1, 5
print("\nКвадраты чисел от", a, "до", b)
for square in squares(a, b):
    print(square)

n = 5
print("\nЧисла от", n, "до 0")
for num in countdown(n):
    print(num)
