"""
ДЗ презентации 4, повышенный уровень, задача 1.
Время: 25–35 минут.

Тема: Decimal, ROUND_HALF_UP.

Условие:
    Запросите цену (строка, например "19.99"), количество
    и налоговую ставку в процентах. Вычислите итоговую стоимость
    с помощью Decimal, округлив до двух знаков по ROUND_HALF_UP.

Пример:
    In: 19.99
    In: 3
    In: 13
    Out: Overall: 67.77
"""
from decimal import Decimal, ROUND_HALF_UP


def total() -> str:
    price = input("Введите цену: ")
    qty = int(input("Введите количество: "))
    tax = input("Введите налоговую ставку в процентах: ")
    overall = (Decimal(price) * qty * (1 + Decimal(tax) / 100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(f"Overall: {overall}")

#if __name__ == "__main__":
    #assert total("19.99", 3, "13") == "Overall: 67.77"
    #assert total("100", 1, "0") == "Overall: 100.00"
    #print("task_01 (p4 advanced): тесты пройдены")

"""
ДЗ презентации 4, повышенный уровень, задача 2.
Время: 25–35 минут.

Тема: Fraction.

Условие:
    Запросите две дроби в формате "числитель/знаменатель".
    Сложите их с помощью Fraction и выведите несократимую дробь.

Пример:
    In: 1/3
    In: 1/6
    Out: 1/2
"""
from fractions import Fraction

def sum_fractions() -> str:
    f1 = input("Введите первую дробь: ")
    f2 = input("Введите вторую дробь: ")
    result = Fraction(f1) + Fraction(f2)
    print(result)

#if __name__ == "__main__":
    #assert sum_fractions("1/3", "1/6") == "1/2"
    #assert sum_fractions("1/2", "1/2") == "1"
    #print("task_02 (p4 advanced): тесты пройдены")