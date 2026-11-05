# task1.py — Домашняя работа 6, базовый уровень.
# Задача 1. Валидатор пользовательских данных.


# ============================================================
# Задача 1. Валидатор пользовательских данных
# ============================================================
# При регистрации проверяем логин и возраст.
#
# Правила:
#   - логин не пустой;
#   - длина логина от 3 до 20 символов;
#   - возраст от 18 до 120 включительно.
#
# Подзадачи:
#   1.1. Вернуть True, если логин корректен.
#   1.2. Вернуть True, если возраст корректен.
#   1.3. Вернуть True, если оба условия выполнены.
#   1.4. Вернуть строку с первой ошибкой:
#        "empty login", "short login", "long login",
#        "too young", "too old", "ok".

def hw_1_1_login_ok(login: str) -> bool:
    """Вернуть True, если логин от 3 до 20 символов."""
    return 3 <= len(login) <= 20

def hw_1_2_age_ok(age: int) -> bool:
    """Вернуть True, если 18 <= age <= 120."""
    return 18 <= age <= 120


def hw_1_3_both_ok(login: str, age: int) -> bool:
    """Вернуть True, если логин и возраст корректны."""
    return hw_1_1_login_ok(login) and hw_1_2_age_ok(age)


def hw_1_4_first_error(login: str, age: int) -> str:
    """Вернуть текст первой ошибки или 'ok'."""
    if login == "":
        return "empty login"
    elif hw_1_1_login_ok(login) == False and len(login) < 3:
        return "short login"
    elif hw_1_1_login_ok(login) == False and len(login) > 20:
        return "long login"
    elif hw_1_2_age_ok(age) == False and age < 18:
        return "too young"
    elif hw_1_2_age_ok(age) == False and age > 120:
        return "too old"
    elif hw_1_3_both_ok(login, age):
        return "ok"


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_1_1_login_ok("ira") is True
    assert hw_1_1_login_ok("ab") is False
    assert hw_1_1_login_ok("a" * 21) is False
    assert hw_1_2_age_ok(18) is True
    assert hw_1_2_age_ok(120) is True
    assert hw_1_2_age_ok(17) is False
    assert hw_1_3_both_ok("ira", 20) is True
    assert hw_1_3_both_ok("ab", 20) is False
    assert hw_1_4_first_error("", 20) == "empty login"
    assert hw_1_4_first_error("ab", 20) == "short login"
    assert hw_1_4_first_error("a" * 21, 20) == "long login"
    assert hw_1_4_first_error("ira", 17) == "too young"
    assert hw_1_4_first_error("ira", 121) == "too old"
    assert hw_1_4_first_error("ira", 20) == "ok"

    print("task1: все assert-тесты пройдены.")


    # task2.py — Домашняя работа 6, базовый уровень.
# Задача 2. Классификатор оценок и стипендия.


# ============================================================
# Задача 2. Классификатор оценок и стипендия
# ============================================================
# По баллу (0..100) определяем оценку и стипендию.
#
# Оценки:
#   - 90..100 -> "A"
#   - 75..89  -> "B"
#   - 60..74  -> "C"
#   - 0..59   -> "F"
#
# Стипендия:
#   - "A" -> True
#   - иначе -> False
#
# Подзадачи:
#   2.1. Вернуть оценку по баллу.
#   2.2. Вернуть True, если балл даёт стипендию.
#   2.3. Вернуть True, если балл валиден (0..100).
#   2.4. Вернуть строку вида "A:yes", "B:no" и т.п.

def hw_2_1_grade(score: int) -> str:
    """Вернуть 'A', 'B', 'C' или 'F'."""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score <= 59:
        return "F"


def hw_2_2_scholarship(score: int) -> bool:
    """Вернуть True, если оценка 'A'."""
    return hw_2_1_grade(score) == "A"


def hw_2_3_score_ok(score: int) -> bool:
    """Вернуть True, если 0 <= score <= 100."""
    return 0 <= score <= 100


def hw_2_4_grade_line(score: int) -> str:
    """Вернуть строку вида 'A:yes' или 'B:no'."""
    return f"{hw_2_1_grade(score)}:{'yes' if hw_2_2_scholarship(score) else 'no'}"


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_2_1_grade(95) == "A"
    assert hw_2_1_grade(80) == "B"
    assert hw_2_1_grade(65) == "C"
    assert hw_2_1_grade(30) == "F"
    assert hw_2_2_scholarship(95) is True
    assert hw_2_2_scholarship(80) is False
    assert hw_2_3_score_ok(0) is True
    assert hw_2_3_score_ok(100) is True
    assert hw_2_3_score_ok(101) is False
    assert hw_2_4_grade_line(95) == "A:yes"
    assert hw_2_4_grade_line(80) == "B:no"

    print("task2: все assert-тесты пройдены.")

    # task3.py — Домашняя работа 6, базовый уровень.
# Задача 3. Разбор строки лога.


# ============================================================
# Задача 3. Разбор строки лога
# ============================================================
# На вход приходит строка вида "LEVEL:message".
# Например: "INFO:start", "ERROR:disk full".
#
# Подзадачи:
#   3.1. Вернуть уровень (до ':').
#   3.2. Вернуть сообщение (после ':').
#   3.3. Вернуть True, если уровень — "ERROR" или "WARN".
#   3.4. Вернуть True, если сообщение не пустое и не содержит пробелов
#        в начале/конце.
#   3.5. Нормализовать: уровень в верхнем регистре, сообщение в нижнем,
#        склеить через ':'.

def hw_3_1_level(line: str) -> str:
    """Вернуть уровень до ':'."""
    return line.split(":")[0]


def hw_3_2_message(line: str) -> str:
    """Вернуть сообщение после ':'."""
    return line.split(":")[1]


def hw_3_3_is_alert(line: str) -> bool:
    """Вернуть True, если уровень 'ERROR' или 'WARN'."""
    return hw_3_1_level(line).upper() == "ERROR" or hw_3_1_level(line).upper() == "WARN"


def hw_3_4_message_clean(line: str) -> bool:
    """Вернуть True, если сообщение не пустое и без пробелов по краям."""
    return hw_3_2_message(line) != "" and line == line.strip()


def hw_3_5_normalize(line: str) -> str:
    """Вернуть 'LEVEL:message' в нормализованном виде."""
    if hw_3_4_message_clean(line) == False:
        return False
    else:
        return f"{hw_3_1_level(line).upper()}:{hw_3_2_message(line).lower()}"


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_3_1_level("INFO:start") == "INFO"
    assert hw_3_2_message("INFO:start") == "start"
    assert hw_3_3_is_alert("ERROR:disk full") is True
    assert hw_3_3_is_alert("WARN:low memory") is True
    assert hw_3_3_is_alert("INFO:start") is False
    assert hw_3_4_message_clean("INFO:start") is True
    assert hw_3_4_message_clean("INFO:") is False
    assert hw_3_4_message_clean("INFO: start ") is False
    assert hw_3_5_normalize("info:START") == "INFO:start"
    assert hw_3_5_normalize("Error:DISK Full") == "ERROR:disk full"

    print("task3: все assert-тесты пройдены.")


    # task4.py — Домашняя работа 6, базовый уровень.
# Задача 4. Снапшоты значений.


# ============================================================
# Задача 4. Снапшоты значений
# ============================================================
# Есть список чисел (снапшоты метрики). Нужно описать каждый снапшот.
#
# Подзадачи:
#   4.1. Вернуть True, если значение положительное и чётное.
#   4.2. Вернуть True, если значение отрицательное и делится на 3.
#   4.3. Вернуть True, если значение равно 0.
#   4.4. Вернуть строку-описание:
#        "positive even", "positive odd",
#        "negative div3", "negative not div3",
#        "zero".
#   4.5. Вернуть True, если ВСЕ снапшоты в списке положительные.

def hw_4_1_pos_even(x: int) -> bool:
    """Вернуть True, если x > 0 и x % 2 == 0."""
    return x > 0 and x % 2 == 0


def hw_4_2_neg_div3(x: int) -> bool:
    """Вернуть True, если x < 0 и x % 3 == 0."""
    return x < 0 and x % 3 == 0


def hw_4_3_is_zero(x: int) -> bool:
    """Вернуть True, если x == 0."""
    return x == 0


def hw_4_4_describe(x: int) -> str:
    """Вернуть описание значения."""
    if x > 0 and hw_4_1_pos_even(x):
        return "positive even"
    elif x > 0 and not hw_4_1_pos_even(x):
        return "positive odd"
    elif x < 0 and hw_4_2_neg_div3(x):
        return "negative div3"
    elif x < 0 and not hw_4_2_neg_div3(x):
        return "negative not div3"
    elif hw_4_3_is_zero(x):
        return "zero"


def hw_4_5_all_positive(values: list[int]) -> bool:
    """Вернуть True, если все значения > 0."""
    return min(values) > 0


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_4_1_pos_even(4) is True
    assert hw_4_1_pos_even(3) is False
    assert hw_4_2_neg_div3(-9) is True
    assert hw_4_2_neg_div3(-4) is False
    assert hw_4_3_is_zero(0) is True
    assert hw_4_3_is_zero(1) is False
    assert hw_4_4_describe(4) == "positive even"
    assert hw_4_4_describe(3) == "positive odd"
    assert hw_4_4_describe(-9) == "negative div3"
    assert hw_4_4_describe(-4) == "negative not div3"
    assert hw_4_4_describe(0) == "zero"
    assert hw_4_5_all_positive([1, 2, 3]) is True
    assert hw_4_5_all_positive([1, -2, 3]) is False

    print("task4: все assert-тесты пройдены.")


    # task5.py — Домашняя работа 6, базовый уровень.
# Задача 5. Мини-парсер данных (строки + regex).


# ============================================================
# Задача 5. Мини-парсер данных (строки + regex)
# ============================================================
# На вход приходит строка с парами "ключ=значение", разделёнными ';'.
# Например: "name=Ira;age=20;city=Moscow".
#
# Подзадачи:
#   5.1. Вернуть список ключей.
#   5.2. Вернуть список значений.
#   5.3. Вернуть True, если все значения непустые.
#   5.4. Вернуть True, если строка содержит хотя бы одну цифру.
#   5.5. Вернуть True, если все ключи состоят только из латинских букв.

import re


def hw_5_1_keys(data: str) -> list[str]:
    """Вернуть список ключей."""
    res = dict(x.split("=") for x in data.split(";"))
    return list(res.keys())


def hw_5_2_values(data: str) -> list[str]:
    """Вернуть список значений."""
    res = dict(x.split("=") for x in data.split(";"))
    return list(res.values())


def hw_5_3_all_nonempty(data: str) -> bool:
    """Вернуть True, если все значения непустые."""
    return all(x != "" for x in hw_5_2_values(data))


def hw_5_4_has_digit(data: str) -> bool:
    """Вернуть True, если в строке есть хотя бы одна цифра."""
    return any(x.isdigit() for x in data)


def hw_5_5_keys_latin(data: str) -> bool:
    """Вернуть True, если все ключи — только латинские буквы."""
    keys_list = hw_5_1_keys(data)
    return all(x.isascii() for x in keys_list)


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    data = "name=Ira;age=20;city=Moscow"
    assert hw_5_1_keys(data) == ["name", "age", "city"]
    assert hw_5_2_values(data) == ["Ira", "20", "Moscow"]
    assert hw_5_3_all_nonempty(data) is True
    assert hw_5_3_all_nonempty("name=;age=20") is False
    assert hw_5_4_has_digit(data) is True
    assert hw_5_4_has_digit("name=Ira;city=Moscow") is False
    assert hw_5_5_keys_latin(data) is True
    assert hw_5_5_keys_latin("имя=Ira") is False

    print("task5: все assert-тесты пройдены.")


    