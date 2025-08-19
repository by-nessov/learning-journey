nums = [2, -2, 4, 9, 0, -3]

print("Исходный список:", nums)

# 1) Фильтрация положительных чисел
positives = []

for n in nums:
    if n > 0:
        positives.append(n)
print("Положительные:", positives)

# 2) Квадраты всех чисел (два способа)

squares = []
for sq in nums:
    squares.append(sq*sq)
print("Квадраты через  append:", squares)

print("-" * 30)

fruits = ["Манго", "апельсин", "грейпфрут"]
print("Перебор fruits с индексами, начиная с 1:")
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")