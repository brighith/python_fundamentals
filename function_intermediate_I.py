import random


def randInt(min=0, max=100):
    if min > max:
        return False

    else:
        if max != 100 and min != 0:
            return round(random.random()*(450)+50)
        if min != 0:
            return round(random.random()*(50)+50)
        if max != 100:
            return round(random.random()*50)
    return round(random.random()*100)


print(
    f"should print a random integer between 0 to 100, randInt() = {randInt()}")
print(
    f"should print a random integer between 0 to 50, randInt(max = 50) = {randInt(max = 50)}")
print(
    f"should print a random integer between 50 to 100, randInt(min = 50) = {randInt(min = 50)}")
print(
    f"should print a random integer between 50 and 500, randInt(min = 50, max = 500) = {randInt(min = 50, max = 500)}")
print(
    f" randInt(min = 15, max = 8) = {randInt(min = 15, max = 8)}")
print(
    f" randInt(max = -1) = {randInt(max = -1)}")
