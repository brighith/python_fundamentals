class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self


# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
# run each of the methods a few more times and check the result!

adding = MathDojo()
a1 = adding.add(4).add(4, 7, 9, 4).add(-1, 9, 5, 1, 0).result
print(a1)

subtracting = MathDojo()
a2 = subtracting.subtract(3).subtract(3, 8).subtract(9, 7, 3).result
print(a2)
