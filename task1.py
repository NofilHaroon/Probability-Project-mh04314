import random
import matplotlib.pyplot as plt
import numpy

# prob = [0.05, 0.95]  # Probability to move left or right
# begin = 2  # begin at 2
# positions = [begin]
# for i in range(1, 1000):
#     rr = random.random()
#     left = rr < prob[0] and positions[-1] > 1
#     right = rr > prob[1] and positions[-1] < 4
#     positions.append(positions[-1] - left + right)
# plt.plot(positions)
# plt.show()


def task1(prob, begin, position):
    x = list()
    x.append(begin)
    y = list(range(position + 1))

    for gen_random in numpy.random.random(position):
        if gen_random < prob:
            x.append(x[-1] - 1)
        if gen_random > prob:
            x.append(x[-1] + 1)

    plt.plot(x, y, 'm-')
    plt.show()


# Different cases each with 100 moves for a larger sample size
# First case
# Beginning from 0 with equal probability to move in either direction
# task1(0.50, 0, 100)

# Second case
# Beginning from 0 with unequal probability to move in either direction (favoring right)
task1(0.30, 0, 100)

# Third case
# Beginning from 0 with unequal probability to move in either direction (favoring left)
# task1(0.70, 0, 100)

# Fourth case
# Beginning from 0 with 0 probability to move in left direction (only right)
# task1(0.00, 0, 100)
