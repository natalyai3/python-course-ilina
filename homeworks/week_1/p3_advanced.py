"""
ДЗ презентации 3, повышенный уровень, задача 1.
Время: 25–35 минут.

Тема: улучшение O(n^2) до O(n) через set.

Условие:
    Реализуйте has_duplicates_fast за O(n) по времени
    и O(n) по памяти.

Ограничения:
    0 <= n <= 100_000
    -10^9 <= nums[i] <= 10^9
"""

def has_duplicates_fast(nums: list) -> bool:
    x = set()
    result = False
    for n in nums:
        if n in x:
            result = True
            pass
        else:
            x.add(n)
    return result


if __name__ == "__main__":
    assert has_duplicates_fast([]) is False
    assert has_duplicates_fast([1]) is False
    assert has_duplicates_fast([1, 2, 3]) is False
    assert has_duplicates_fast([1, 2, 1]) is True
    assert has_duplicates_fast([5, 5]) is True

    data = list(range(100_000))
    assert has_duplicates_fast(data) is False
    data2 = list(range(99_999)) + [0]
    assert has_duplicates_fast(data2) is True

    print("task_01 (p3 advanced): тесты пройдены")

"""
ДЗ презентации 3, повышенный уровень, задача 2.
Время: 25–35 минут.

Тема: O(n) поиск min и max.

Условие:
    Реализуйте функцию min_max(nums) -> (min_val, max_val)
    за O(n).

Пример:
    In: [3, 1, 4, 1, 5, 9, 2, 6]
    Out: (1, 9)
"""

def min_max(nums: list) -> tuple:
    x_min = nums[0]
    x_max = nums[0]
    for n in nums:
        if n < x_min:
            x_min = n
        elif n > x_max:
            x_max = n
    return (x_min, x_max)

if __name__ == "__main__":
    assert min_max([3, 1, 4, 1, 5, 9, 2, 6]) == (1, 9)
    assert min_max([7]) == (7, 7)
    assert min_max([-5, -1, -10]) == (-10, -1)
    print("task_02 (p3 advanced): тесты пройдены")