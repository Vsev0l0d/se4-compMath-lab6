import matplotlib.pyplot as plt
import numpy as np


def graph(data, solution, title: str):
    data_x, data_y = data
    plt.figure()
    plt.title = title
    plt.grid(True)

    plt.scatter(data_x, data_y, s=20, zorder=10)
    plt.plot(data_x, data_y, zorder=5, label=title)

    x_linspace = np.linspace(data_x[0], data_x[-1], 100)
    exact_y = [solution(x) for x in x_linspace]
    plt.plot(x_linspace, exact_y, zorder=5, label="Точное решение")

    plt.legend(fontsize='x-small')
    plt.savefig(f'{title.replace(" ", "_")}.png')
    plt.show()
