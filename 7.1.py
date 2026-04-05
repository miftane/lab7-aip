# 7.1.py
numbers = [3, 7, 12, 5, 9]
user_number = int(input("Введите число: "))

print(f"Исходный список: {numbers}")
print(f"Ваше число: {user_number}")

if user_number in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа")
