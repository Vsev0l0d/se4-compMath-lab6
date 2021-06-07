from tabulate import tabulate


def rungeKutte(x0, y0, h, x_last, f, solution, eps=None, log=False):
    xValues = [x0]
    yValues = [y0]
    calculation_table = []

    while xValues[-1] <= x_last:
        prX = xValues[-1]
        prY = yValues[-1]
        k1 = h * f(prX, prY)
        k2 = h * f(prX + 0.5 * h, prY + 0.5 * k1)
        k3 = h * f(prX + 0.5 * h, prY + 0.5 * k2)
        k4 = h * f(prX + h, prY + k3)
        calculation_table.append([len(xValues), prX, k1, k2, k3, k4, prY, f(prX, prY), solution(prX)])
        if prX == x_last:
            break
        yValues.append(prY + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4))
        xValues.append(round(prX + h, 5))

    if log:
        field_names = ["i", "x", "k1", "k2", "k3", "k4", "y", "F(x,y)", "Точное решение"]
        print(tabulate(calculation_table, field_names, tablefmt='grid', floatfmt='2.4f'))
    return xValues, yValues


def milne(x0, y0, h, x_last, func, solution, eps, log=False):
    if x0 + 3 * h > x_last:
        raise Exception("Необходимо от 4 значений x")
    xValues, yValues = rungeKutte(x0, y0, h, round(x0 + 3 * h, 5), func, solution, log=log)
    calculation_table = []
    f = []
    for i in range(1, 4):
        f.append(func(xValues[i], yValues[i]))
    x = xValues[-1] + h
    i = 5

    while x <= x_last:
        xValues.append(round(x, 5))

        y_predicted = yValues[-4] + 4 * h * (2 * f[0] - f[1] + 2 * f[2]) / 3
        new_f = func(x, y_predicted)
        y_corrected = yValues[-2] + h * (f[1] + 4 * f[2] + new_f) / 3
        while abs(y_corrected - y_predicted) > eps:
            y_predicted = y_corrected
            new_f = func(x, y_predicted)
            y_corrected = yValues[-2] + h * (f[1] + 4 * f[2] + new_f) / 3
        yValues.append(y_predicted)
        f = f[1:]
        f.append(new_f)

        calculation_table.append([i, x, y_predicted, new_f, solution(x)])
        x += h
        i += 1

    if log:
        field_names = ["i", "x", "y", "F(x,y)", "Точное решение"]
        print(tabulate(calculation_table, field_names, tablefmt='grid', floatfmt='2.4f'))
    return xValues, yValues
