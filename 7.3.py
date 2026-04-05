# 7.3.py
days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

weekend_count = int(input("Сколько выходных на неделе вы хотите? "))

weekend_days = list(days[-weekend_count:])
work_days = list(days[:-weekend_count])

print(f"Ваши выходные дни: {', '.join(weekend_days)}")
print(f"Ваши рабочие дни: {', '.join(work_days)}")
