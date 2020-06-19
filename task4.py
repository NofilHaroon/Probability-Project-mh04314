import random
import matplotlib.pyplot as plt
import numpy


def task4(prob, begin, position):
    x = list()
    x.append(begin)
    y = list(range(position + 1))

    for gen_random in numpy.random.random(position):
        if gen_random < prob:
            x.append(x[-1] - random.random())
        if gen_random > prob:
            x.append(x[-1] + random.random())

    plt.plot(x, y, 'm-')
    plt.show()


# Beginning from 0 with equal probability to move in either direction
task4(0.50, 0, 100)
