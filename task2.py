import random
import matplotlib.pyplot as plt


def task2(prob_person1, prob_person2, position_person1, position_person2):
    x1 = list()
    x1.append(position_person1)
    x2 = list()
    x2.append(position_person2)

    # run loop until both people meet at a certain position in time.
    moves = 0
    while True:
        if x1[-1] == x2[-1]:
            print("It takes " + str(moves) +
                  " seconds for these two people to cross their paths.")
            break

        gen_random = random.random()
        if gen_random > prob_person1:
            x1.append(x1[-1] + 1)
        if gen_random < prob_person1:
            x1.append(x1[-1] - 1)
        gen_random = random.random()
        if gen_random > prob_person2:
            x2.append(x2[-1] + 1)
        if gen_random < prob_person2:
            x2.append(x2[-1] - 1)

        moves += 1

    y = list(range(moves + 1))

    plt.plot(x1, y, 'm-', label='1st Person')
    plt.plot(x2, y, 'c-', label='2nd Person')
    plt.legend()
    plt.show()


# First case
# Person 1 begins at 0 and person 2 begins at 10
# both have equal probability to move in either direction (left or right)
task2(0.5, 0.5, 0, 10)

# Second case
# Person 1 begins at 0 and person 2 begins at 10
# both people have a
#  tendency to favor movement in opposite directions (left or right)
# takes longer for them to cross paths
# task2(0.3, 0.7, 0, 10)
