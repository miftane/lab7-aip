# 7.2.py
from collections import Counter

my_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]
counter = Counter(my_list)

duplicates = [item for item, count in counter.items() if count > 1]
print(f"Список: {my_list}")

if duplicates:
    print(f"Повторяющиеся элементы: {duplicates}")
else:
    print("Повторяющихся элементов нет")
