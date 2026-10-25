"""
ДЗ презентации 5, повышенный уровень, задача 1.
Время: 25–35 минут.

Тема: дробный рюкзак.

Условие:
    items — список кортежей (weight, value).
    Верните максимальную суммарную стоимость.

Пример:
    capacity = 50
    items = [(10, 60), (20, 100), (30, 120)]
    Ответ: 240.0
"""

def fractional_knapsack(capacity: float, items: list) -> float:
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    total = 0.0
    for weight, value in items:
        if capacity >= weight:
            total += value
            capacity -= weight
            pass
        else:
            total += value * (capacity / weight)
            capacity = 0
            pass
    return total


if __name__ == "__main__":
    items = [(10, 60), (20, 100), (30, 120)]
    assert abs(fractional_knapsack(50, items) - 240.0) < 1e-9
    assert fractional_knapsack(0, items) == 0.0
    print("task_01 (p5 advanced): тесты пройдены")

    """
ДЗ презентации 5, повышенный уровень, задача 2.
Время: 25–35 минут.

Тема: минимальное число платформ.

Условие:
    Даны arrivals и departures поездов.
    Верните минимальное число платформ.

Пример:
    arrivals   = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    Ответ: 3
"""

def min_platforms(arrivals: list, departures: list) -> int:
    events = [(t, 1) for t in arrivals] + [(t, -1) for t in departures]
    events.sort()
    current = 0
    best = 0
    for _, delta in events:
        current += delta
        if current > best:
            best = current
        pass
    return best


if __name__ == "__main__":
    assert min_platforms([], []) == 0
    assert min_platforms([900], [910]) == 1
    assert min_platforms(
        [900, 940, 950, 1100, 1500, 1800],
        [910, 1200, 1120, 1130, 1900, 2000]
    ) == 3
    assert min_platforms([100, 200, 300], [150, 250, 350]) == 1
    print("task_02 (p5 advanced): тесты пройдены")