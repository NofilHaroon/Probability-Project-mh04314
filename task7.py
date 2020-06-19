import math
import numpy
import matplotlib.pyplot as plt


def task5():
    x = list()
    y = list()
    x.append(0)
    y.append(0)

    angle1 = numpy.linspace(0, 2*math.pi, 200)
    radius1 = 10  # area of circle is 100 units sq.

    x1 = radius1 * numpy.cos(angle1)
    x2 = radius1 * numpy.sin(angle1)

    angle2 = numpy.cumsum(numpy.random.uniform(0, math.pi * 2, size=25))
    radius2 = numpy.random.choice([0.0, 1.0, 0.5], 1000)

    for i, j in zip(angle2, radius2):
        x_position = j * math.cos(i)
        y_position = j * math.sin(i)
        if (x[-1] + x_position) ** 2 + (y[-1] + y_position) ** 2 <= 100:
            x.append(x[-1] + x_position)
            y.append(y[-1] + y_position)

    axes = plt.subplots(1)[1]
    axes.plot(x1, x2, 'm-')
    axes.plot(x, y, 'c-')
    axes.set_aspect('equal')
    plt.show()


task5()
