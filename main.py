from graph import *
from boilerplate import *
from methods import *

methods = (
    (rungeKutte, 'Метод Рунге-Кутта 4-го порядка'),
    (milne, 'Метод Милна')
)

functions = (
    (lambda x, y: 2 * x * y, 'y\' = 2xy', lambda x: math.exp(x ** 2)),
    (lambda x, y: 2 * x - y + x ** 2, 'y\' = 2x - y + x^2', lambda x: x ** 2),
    (lambda x, y: (x - y) ** 2 + 1, 'y\' = (x - y)^2 + 1', lambda x: x)
)

if __name__ == '__main__':
    print('Выберите функцию ')
    print_indexed_list(map(lambda tup: tup[1], functions))
    index = int(number_input('Введите номер: ', min=1, max=len(functions)))
    f, text, solution = functions[index - 1]
    x0, x_last = float_interval_choice()
    y0 = number_input(f'Введите y({x0}): ')
    h = number_input('Введите h: ')
    eps = number_input('Введите eps: ')

    for solve, name in methods:
        try:
            print(f'\n{name}: ')
            xValues, yValues = solve(x0, y0, h, x_last, f, solution, eps, log=True)

            X2h, Y2h = solve(x0, y0, h / 2, x_last, f, solution, eps)
            R = []
            for i in range(len(yValues)):
                R.append((yValues[i] - Y2h[i * 2]) / (2 ** 4 - 1))
            print(f'Оценки точности по правилу Рунге:\n{R}')

            graph([xValues, yValues], solution, name)
        except Exception as e:
            print(e)
