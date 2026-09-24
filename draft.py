def seconds_to_hms(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return(f'{hours:02}:{minutes:02}:{seconds:02}')

seconds_to_hms(3661)

def sum_digits(n: int) -> int:
    res = n // 100 + ((n // 10) % 10) + n % 10
    print(int(res))

#sum_digits(456)

def coin_change(amount: int) -> dict:
    num_50 = amount // 50
    num_10 = (amount - 50 * num_50) // 10
    num_5 = (amount - 50 * num_50 - 10 * num_10) // 5
    num_1 = amount - num_50 * 50 - num_10 * 10 - num_5 * 5
    res = {50: num_50, 10: num_10, 5: num_5, 1: num_1}
    print(res)
#coin_change(87)