from datetime import datetime
try:
    amount = float(input("Введите сумму (включая НДС): "))
    vat_rate = float(input("Введите ставку НДС (%): "))
    vat_fraction = vat_rate / (100 + vat_rate)
    vat_amount = amount * vat_fraction
    result = f"Сумма: {amount:.2f} руб.\nСтавка НДС: {vat_rate}%\nСумма НДС: {vat_amount:.2f} руб.\n"
    print(result)
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {result}\n")
    print("Результат сохранён в файл result.txt")
except ValueError:
    print("Ошибка: введите числовые значения.")