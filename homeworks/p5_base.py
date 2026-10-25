"""
ДЗ презентации 5, базовый уровень, задача 1.
Время: 20–30 минут.

Тема: жадный размен монет.

Условие:
    Реализуйте жадный размен для номиналов [50, 10, 5, 1].
    Верните количество монет.

Пример:
    In: 87
    Out: 7

Подсказки:
    1. Номиналы удобно хранить в списке: coins = [50, 10, 5, 1].
    2. Жадная стратегия: берём самую крупную монету, которая
       не превышает остаток, вычитаем её и повторяем.
    3. Пока amount >= coin:
           amount -= coin
           count += 1
    4. Пройдитесь по всем номиналам и верните count.
"""

def min_coins(amount: int) -> int:
    coins = [50, 10, 5, 1]
    count = 0
    for c in coins:
        while amount >= c:
            count += 1
            amount -= c
    return count


if __name__ == "__main__":
    print(min_coins(87))   # 7
    print(min_coins(0))    # 0
    print(min_coins(100))  # 2

"""
ДЗ презентации 5, базовый уровень, задача 2.
Время: 20–30 минут.

Тема: жадный выбор интервалов.

Условие:
    Реализуйте выбор максимального количества
    непересекающихся интервалов.

Пример:
    intervals = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11)]
    Ответ: 4

Подсказки:
    1. Отсортируйте интервалы по времени окончания:
           intervals.sort(key=lambda x: x[1])
    2. Заведите last_end = float("-inf") — конец последнего
       выбранного интервала.
    3. Пройдитесь по интервалам:
           for start, end in intervals:
               if start >= last_end:
                   count += 1
                   last_end = end
    4. Верните count.
"""

def max_intervals(intervals: list) -> int:
    count = 0
    last_end = float("-inf")
    intervals.sort(key=lambda x: x[1])
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
            pass
    return count


if __name__ == "__main__":
    data = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11)]
    print(max_intervals(data))  # 4