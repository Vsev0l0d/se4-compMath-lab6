from tabulate import tabulate


def rungeKutte(x0, y0, h, x_last, f):
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
        calculation_table.append([prX, k1, k2, k3, k4, prY])
        yValues.append(prY + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4))
        xValues.append(round(prX + h, 5))

    print(tabulate(calculation_table, ["x", "k1", "k2", "k3", "k4", "y"], tablefmt='grid', floatfmt='2.4f'))
    return xValues, yValues


def milne(x0, y0, h, x_last, f):
    xValues = [x0]
    yValues = [y0]
    return xValues, yValues
