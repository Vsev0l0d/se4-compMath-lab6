import math


def number_input(prompt: str, min=-math.inf, max=math.inf) -> float:
    while True:
        ans = input(prompt)
        try:
            num = float(ans)
            if num < min or num > max:
                print(f'Число должно быть в интервале [{round(min, 1)}, {round(max, 1)}].')
                continue
            return num
        except:
            continue


def float_interval_choice() -> [float, float]:
    while True:
        ans = input('Введите интервал: ').split()
        try:
            left, right = float(ans[0]), float(ans[1])
            if left >= right:
                print('Введите корректный интервал.')
                continue
            return left, right
        except:
            print('Введите корректный интервал.')
            continue


def print_indexed_list(indexed_list, start=1):
    for index, item in enumerate(indexed_list, start=start):
        print(f'{index}. {item}')

