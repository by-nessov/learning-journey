revenue = float(input("Введите выручку:"))
expenses = float(input("Введите ваши расходы:"))
percent = "%"
marginality1 = int(revenue - expenses)
marginality_total = int(marginality1 / revenue * 100)
print("Учитывая ваши выручку и расходы, маржинальность составляет", marginality_total, percent)