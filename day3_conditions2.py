from datetime import datetime
revenue = float(input("Введите выручку:"))
expenses = float(input("Введите ваши расходы:"))
percent = "%"
profit = int(revenue - expenses)
marginality = round((revenue - expenses) / revenue * 100, 2)
if marginality >= 50:
    message = f"У вас прекрасная маржинальность! Она составляет: {marginality}%"
elif marginality > 30:
    message = f"С вашей маржинальностью можно работать и расти! Она составляет: {marginality}%"
else:
    message = f"Ваша маржинальность слишком мала, пересмотрите бизнес-стратегию. Ваша маржа всего: {marginality}%"
print(message)
with open("marginality.txt", "a", encoding="utf-8") as f:
    f.write(f"[{datetime.now()}] {message}\n")