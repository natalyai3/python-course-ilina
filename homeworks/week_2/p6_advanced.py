# task1.py — Домашняя работа 6, продвинутый уровень.
# Задача 1. Валидатор учётных записей.


# ============================================================
# Задача 1. Валидатор учётных записей
# ============================================================
# Проверяем логин, email и возраст при регистрации.
#
# Правила:
#   - логин не пустой;
#   - длина логина от 3 до 20 символов;
#   - логин без пробелов;
#   - email вида "name@domain.xx" (упрощённо: \w+@\w+\.[a-z]{2,3});
#   - возраст от 18 до 120 включительно.
#
# Подзадачи:
#   1.1. Вернуть True, если логин корректен (3..20 и без пробелов).
#   1.2. Вернуть True, если email соответствует шаблону (re.fullmatch).
#   1.3. Вернуть True, если возраст 18..120.
#   1.4. Вернуть True, если корректны все три поля.
#   1.5. Вернуть первую ошибку в порядке:
#        "empty login", "short login", "long login", "space in login",
#        "bad email", "too young", "too old", "ok".

import re


def hw_1_1_login_ok(login: str) -> bool:
    """Вернуть True, если логин корректен."""
    return 3 <= len(login) <= 20 and not any(x.isspace() for x in login)


def hw_1_2_email_ok(email: str) -> bool:
    """Вернуть True, если email подходит под шаблон."""
    return bool(re.fullmatch('\\w+@\w+\.[a-z]{2,3}', email))


def hw_1_3_age_ok(age: int) -> bool:
    """Вернуть True, если 18 <= age <= 120."""
    return 18 <= age <= 120


def hw_1_4_all_ok(login: str, email: str, age: int) -> bool:
    """Вернуть True, если все поля корректны."""
    return hw_1_1_login_ok(login) and hw_1_2_email_ok(email) and hw_1_3_age_ok(age)


def hw_1_5_first_error(login: str, email: str, age: int) -> str:
    """Вернуть текст первой ошибки или 'ok'."""
    if login == "":
        return "empty login"
    elif len(login) < 3:
        return "short login"
    elif len(login) > 20:
        return "long login"
    elif any(x.isspace() for x in login):
        return "space in login"
    elif not hw_1_2_email_ok(email):
        return "bad email"
    elif age < 18:
        return "too young"
    elif age > 120:
        return "too old"
    else:
        return "ok"


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_1_1_login_ok("ira") is True
    assert hw_1_1_login_ok("ab") is False
    assert hw_1_1_login_ok("a b c") is False
    assert hw_1_1_login_ok("a" * 21) is False
    assert hw_1_2_email_ok("a@b.ru") is True
    assert hw_1_2_email_ok("a@b") is False
    assert hw_1_2_email_ok("a@b.russia") is False
    assert hw_1_3_age_ok(18) is True
    assert hw_1_3_age_ok(121) is False
    assert hw_1_4_all_ok("ira", "a@b.ru", 20) is True
    assert hw_1_4_all_ok("ira", "a@b", 20) is False
    assert hw_1_5_first_error("", "a@b.ru", 20) == "empty login"
    assert hw_1_5_first_error("ab", "a@b.ru", 20) == "short login"
    assert hw_1_5_first_error("a" * 21, "a@b.ru", 20) == "long login"
    assert hw_1_5_first_error("a b", "a@b.ru", 20) == "space in login"
    assert hw_1_5_first_error("ira", "a@b", 20) == "bad email"
    assert hw_1_5_first_error("ira", "a@b.ru", 17) == "too young"
    assert hw_1_5_first_error("ira", "a@b.ru", 121) == "too old"
    assert hw_1_5_first_error("ira", "a@b.ru", 20) == "ok"

    print("task1 (advanced): все assert-тесты пройдены.")


# task2.py — Домашняя работа 6, продвинутый уровень.
# Задача 2. Условные премии и категории сотрудников.


# ============================================================
# Задача 2. Условные премии и категории сотрудников
# ============================================================
# По стажу и оценке performance (0..100) определяем категорию
# и премию.
#
# Категории:
#   - "senior": стаж >= 5 и оценка >= 80;
#   - "middle": стаж >= 2 и оценка >= 60;
#   - "junior": иначе.
#
# Премия (в процентах от оклада):
#   - senior и оценка >= 95 -> 30;
#   - senior                 -> 20;
#   - middle и оценка >= 75  -> 15;
#   - middle                 -> 10;
#   - junior                 -> 0.
#
# Подзадачи:
#   2.1. Вернуть категорию.
#   2.2. Вернуть процент премии.
#   2.3. Вернуть True, если стаж и оценка валидны
#        (стаж >= 0, 0 <= оценка <= 100).
#   2.4. Вернуть строку вида "senior:30" или "junior:0".
#   2.5. Вернуть True, если сотрудник получает премию больше 15%.
#   2.6. Вернуть True, если хотя бы один из двух сотрудников — senior.

def hw_2_1_category(exp: int, perf: int) -> str:
    """Вернуть 'senior', 'middle' или 'junior'."""
    if exp >= 5 and perf >= 80:
        return "senior"
    elif exp >= 2 and perf >= 60:
        return "middle"
    else:
        return "junior"


def hw_2_2_bonus(exp: int, perf: int) -> int:
    """Вернуть процент премии (0/10/15/20/30)."""
    if hw_2_1_category(exp, perf) == "senior":
        return 30 if perf >= 95 else 20
    if hw_2_1_category(exp, perf) == "middle":
        return 15 if perf >= 75 else 10
    else:
        return 0 
 

def hw_2_3_valid(exp: int, perf: int) -> bool:
    """Вернуть True, если стаж и оценка корректны."""
    return exp >= 0 and 0 <= perf <= 100


def hw_2_4_line(exp: int, perf: int) -> str:
    """Вернуть 'категория:премия'."""
    return f"{hw_2_1_category(exp, perf)}:{hw_2_2_bonus(exp, perf)}"


def hw_2_5_big_bonus(exp: int, perf: int) -> bool:
    """Вернуть True, если премия > 15."""
    return hw_2_2_bonus(exp, perf) > 15


def hw_2_6_any_senior(a_exp: int, a_perf: int,
                     b_exp: int, b_perf: int) -> bool:
    """Вернуть True, если хотя бы один — senior."""
    return hw_2_1_category(a_exp, a_perf) == "senior" or hw_2_1_category(b_exp, b_perf) == "senior"


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    assert hw_2_1_category(6, 90) == "senior"
    assert hw_2_1_category(6, 70) == "middle"
    assert hw_2_1_category(1, 90) == "junior"
    assert hw_2_1_category(2, 60) == "middle"
    assert hw_2_2_bonus(6, 95) == 30
    assert hw_2_2_bonus(6, 90) == 20
    assert hw_2_2_bonus(3, 80) == 15
    assert hw_2_2_bonus(3, 70) == 10
    assert hw_2_2_bonus(1, 90) == 0
    assert hw_2_3_valid(0, 0) is True
    assert hw_2_3_valid(-1, 50) is False
    assert hw_2_3_valid(3, 101) is False
    assert hw_2_4_line(6, 95) == "senior:30"
    assert hw_2_4_line(1, 50) == "junior:0"
    assert hw_2_5_big_bonus(6, 95) is True
    assert hw_2_5_big_bonus(6, 80) is True
    assert hw_2_5_big_bonus(3, 80) is False
    assert hw_2_6_any_senior(6, 90, 1, 50) is True
    assert hw_2_6_any_senior(1, 50, 2, 70) is False

    print("task2 (advanced): все assert-тесты пройдены.")

    # task3.py — Домашняя работа 6, продвинутый уровень.
# Задача 3. Парсер логов и классификация событий.


# ============================================================
# Задача 3. Парсер логов и классификация событий
# ============================================================
# На вход приходит строка лога вида
#   "2026-10-05 12:30:45|LEVEL|message"
# Например: "2026-10-05 12:30:45|ERROR|disk full"
#
# Подзадачи:
#   3.1. Вернуть дату (часть до первого '|').
#   3.2. Вернуть уровень (вторая часть).
#   3.3. Вернуть сообщение (третья часть).
#   3.4. Вернуть True, если строка содержит ровно три части
#        и они все непустые.
#   3.5. Вернуть True, если уровень — "ERROR" или "WARN".
#   3.6. Вернуть True, если дата соответствует шаблону YYYY-MM-DD
#        (использовать re.fullmatch по первой части).
#   3.7. Нормализовать лог: уровень в верхнем регистре,
#        сообщение в нижнем, склеить через '|'.

import re


def hw_3_1_date(line: str) -> str:
    """Вернуть дату (до первого '|')."""
    return line.split("|")[0]

def hw_3_2_level(line: str) -> str:
    """Вернуть уровень (вторая часть)."""
    return line.split("|")[1]

def hw_3_3_message(line: str) -> str:
    """Вернуть сообщение (третья часть)."""
    return line.split("|")[2]

def hw_3_4_well_formed(line: str) -> bool:
    """Вернуть True, если ровно три непустые части."""
    return line.count("|") == 2\
          and hw_3_1_date(line) != ""\
              and hw_3_2_level(line) != ""\
                  and hw_3_3_message(line) != ""


def hw_3_5_is_alert(line: str) -> bool:
    """Вернуть True, если уровень 'ERROR' или 'WARN'."""
    return hw_3_2_level(line) in ['ERROR', 'WARN']


def hw_3_6_date_ok(line: str) -> bool:
    """Вернуть True, если дата вида YYYY-MM-DD."""
    return bool(re.fullmatch("\d{4}-\d{2}-\d{2}", hw_3_1_date(line).split()[0])) 


def hw_3_7_normalize(line: str) -> str:
    """Вернуть нормализованный лог."""
    return "|".join([hw_3_1_date(line), hw_3_2_level(line).upper(), hw_3_3_message(line).lower()])


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    line = "2026-10-05 12:30:45|ERROR|disk full"
    assert hw_3_1_date(line) == "2026-10-05 12:30:45"
    assert hw_3_2_level(line) == "ERROR"
    assert hw_3_3_message(line) == "disk full"
    assert hw_3_4_well_formed(line) is True
    assert hw_3_4_well_formed("a|b") is False
    assert hw_3_4_well_formed("a||b") is False
    assert hw_3_5_is_alert(line) is True
    assert hw_3_5_is_alert("2026-10-05 12:30:45|INFO|start") is False
    assert hw_3_6_date_ok("2026-10-05 12:30:45|ERROR|x") is True
    assert hw_3_6_date_ok("2026/10/05 12:30:45|ERROR|x") is False
    assert hw_3_7_normalize("2026-10-05 12:30:45|error|DISK Full") == \
        "2026-10-05 12:30:45|ERROR|disk full"

    print("task3 (advanced): все assert-тесты пройдены.")


# task4.py — Домашняя работа 6, продвинутый уровень.
# Задача 4. Анализ снапшотов метрики.


# ============================================================
# Задача 4. Анализ снапшотов метрики
# ============================================================
# Есть список целых чисел — снапшоты метрики за день.
#
# Подзадачи:
#   4.1. Вернуть True, если значение положительное и чётное.
#   4.2. Вернуть True, если значение отрицательное и делится на 3.
#   4.3. Вернуть True, если значение равно 0.
#   4.4. Вернуть описание значения:
#        "positive even", "positive odd",
#        "negative div3", "negative not div3",
#        "zero".
#   4.5. Вернуть True, если все снапшоты положительные.
#   4.6. Вернуть True, если хотя бы один снапшот равен 0.
#   4.7. Вернуть True, если все снапшоты корректны:
#        положительные чётные, отрицательные делящиеся на 3
#        или ноль.
#   4.8. Вернуть первое "плохое" значение или None, если все хорошие.
#        Плохое — не подходящее ни под одну из категорий:
#        положительное нечётное, отрицательное не делящееся на 3.

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
    if x > 0:
        return "positive even" if hw_4_1_pos_even(x) else "positive odd"
    elif x < 0:
        return "negative div3" if hw_4_2_neg_div3(x) else "negative not div3"
    else:
        return "zero"


def hw_4_5_all_positive(values: list[int]) -> bool:
    """Вернуть True, если все значения > 0."""
    return all(x > 0 for x in values)


def hw_4_6_has_zero(values: list[int]) -> bool:
    """Вернуть True, если есть хотя бы один 0."""
    return any(x == 0 for x in values)


def hw_4_7_all_valid(values: list[int]) -> bool:
    """Вернуть True, если все значения корректны."""
    return all(hw_4_1_pos_even(x) or hw_4_2_neg_div3(x) or hw_4_3_is_zero(x) for x in values)


def hw_4_8_first_bad(values: list[int]) -> int | None:
    """Вернуть первое плохое значение или None."""
    for x in values:
        if not (hw_4_1_pos_even(x) or hw_4_2_neg_div3(x) or hw_4_3_is_zero(x)):
            return x
    return None


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
    assert hw_4_6_has_zero([1, 0, 3]) is True
    assert hw_4_6_has_zero([1, 2, 3]) is False
    assert hw_4_7_all_valid([4, -9, 0]) is True
    assert hw_4_7_all_valid([4, 3, 0]) is False
    assert hw_4_8_first_bad([4, -9, 0, 5]) == 5
    assert hw_4_8_first_bad([4, -9, 0]) is None

    print("task4 (advanced): все assert-тесты пройдены.")



    # task5.py — Домашняя работа 6, продвинутый уровень.
# Задача 5. Парсер и валидатор конфигурации.


# ============================================================
# Задача 5. Парсер и валидатор конфигурации
# ============================================================
# На вход приходит строка с настройками вида "k=v;k=v;...".
# Например: "host=localhost;port=8080;debug=true".
#
# Подзадачи:
#   5.1. Вернуть список ключей.
#   5.2. Вернуть список значений.
#   5.3. Вернуть True, если все значения непустые.
#   5.4. Вернуть True, если все ключи — только латинские буквы/цифры.
#   5.5. Вернуть True, если строка содержит хотя бы одну цифру.
#   5.6. Вернуть True, если есть ключ "port" и его значение — число
#        (re.fullmatch \d+).
#   5.7. Вернуть True, если есть ключ "host" и его значение
#        непустое и без пробелов.
#   5.8. Вернуть словарь {key: value} для всех пар
#        (предполагая корректный ввод).

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


def hw_5_4_keys_latin(data: str) -> bool:
    """Вернуть True, если все ключи — только латинские буквы/цифры."""
    return all(re.fullmatch(r"[a-zA-Z0-9]+", x) for x in hw_5_1_keys(data))


def hw_5_5_has_digit(data: str) -> bool:
    """Вернуть True, если есть хотя бы одна цифра."""
    return any(x.isdigit() for x in data)


def hw_5_6_port_ok(data: str) -> bool:
    """Вернуть True, если port задан числом."""
    return "port" in hw_5_1_keys(data) and hw_5_2_values(data)[hw_5_1_keys(data).index("port")].isdigit()


def hw_5_7_host_ok(data: str) -> bool:
    """Вернуть True, если host непустой и без пробелов."""
    i = hw_5_1_keys(data).index("host")
    return hw_5_2_values(data)[i] != "" and not any(x.isspace() for x in hw_5_2_values(data)[i])


def hw_5_8_to_dict(data: str) -> dict[str, str]:
    """Вернуть словарь пар ключ=значение."""
    return dict(x.split("=") for x in data.split(";"))


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    data = "host=localhost;port=8080;debug=true"
    assert hw_5_1_keys(data) == ["host", "port", "debug"]
    assert hw_5_2_values(data) == ["localhost", "8080", "true"]
    assert hw_5_3_all_nonempty(data) is True
    assert hw_5_3_all_nonempty("host=;port=8080") is False
    assert hw_5_4_keys_latin(data) is True
    assert hw_5_4_keys_latin("хост=localhost") is False
    assert hw_5_5_has_digit(data) is True
    assert hw_5_5_has_digit("host=localhost;debug=true") is False
    assert hw_5_6_port_ok(data) is True
    assert hw_5_6_port_ok("host=localhost;port=abc") is False
    assert hw_5_6_port_ok("host=localhost") is False
    assert hw_5_7_host_ok(data) is True
    assert hw_5_7_host_ok("host=;port=8080") is False
    assert hw_5_7_host_ok("host=local host;port=8080") is False
    assert hw_5_8_to_dict(data) == {
        "host": "localhost",
        "port": "8080",
        "debug": "true",
    }

    print("task5 (advanced): все assert-тесты пройдены.")