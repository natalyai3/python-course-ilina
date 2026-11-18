"""
ДЗ презентации 3, базовый уровень, задача 1.
Время: 10–15 минут.

Тема: алгоритмы, сложность O(n^2).

Условие:
    Дана функция, которая сравнивает два числа nums[i] и nums[j].
    Допишите тело: если они равны, верните True.
    Циклы уже написаны — вписывать их не нужно.

Подсказка:
    Внутри if нужно вернуть True.
"""

def has_duplicates_slow(nums: list) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
            pass
    return False


if __name__ == "__main__":
    data = [1, 2, 3, 2]
    print(has_duplicates_slow(data))   # True
    print(has_duplicates_slow([1, 2, 3]))  # Falsetask_01.py


"""
ДЗ презентации 3, базовый уровень, задача 2.
Время: 20–30 минут.

Тема: оценка сложности.

Условие:
    Определите временную сложность фрагментов.
    Ответ — строка: "O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)".

Фрагмент A:
    for x in items:
        print(x)

Фрагмент B:
    for x in items:
        for y in items:
            print(x, y)

Фрагмент C:
    i = 0
    while i < n:
        i *= 2

Фрагмент D:
    for x in items:
        pass
    for x in items:
        for y in items:
            pass
"""

def complexity_a() -> str:
    return "O(n)"

def complexity_b() -> str:
    return "O(n^2)"

def complexity_c() -> str:
    return "O(log n)"

def complexity_d() -> str:
    return "O(n^2)"

if __name__ == "__main__":
    print(complexity_a(), complexity_b(), complexity_c(), complexity_d())