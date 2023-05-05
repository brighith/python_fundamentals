for x in range(151):
    print(x)
stack = 2
print('coding dojo' if stack >= 5 else 'you r not codint dogo')


# create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x: x ** 2]
# access the value in the list
# print(my_list[2])  # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
print(my_list[2](5))
