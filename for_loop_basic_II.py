# 1 Biggie Size - Given a list, write a function that changes all
# positive numbers in the list to "big".
def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] >= 0:
            arr[i] = "big"
    return arr


print(biggie_size([-1, -8, 9, 0, -4, -7, 6, 4]))


# 2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    # arr.append(count)
    arr[(len(arr)-1)] = count
    return arr


print(count_positives([1, 6, -4, -2, -7, 9]))


# 3 Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


sum = sum_total([1, 2, 3, 4])
print(sum)


#  4 Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum / len(arr)


print(average([1, 2, 3, 4]))

# 5 Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0


def length(list):
    counter = 0
    for i in list:
        counter += 1
    return counter


print(length([37, 2, 1, -9, 7, 8, 9, 2, 3, -9, 0]), "xxxx")
print(length([]))


#  6 minimum - Create a function that takes a list of numbers and returns the minimum
# value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(arr):
    if len(arr) == 0:
        return False
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min


print(minimum([37, 2, 1, -9]), "yyyyyyyy")
print(minimum([]))


#  7 maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(arr):
    if len(arr) == 0:
        return False
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max


print(maximum([-1, 2, 1, -9]))


# 8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, minimum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'minimum': 37, 'length': 4 }
def ultimate_analysis(arr):
    dictionary = {'sumTotal': 0, 'average': 0,
                  'maximum': arr[0], 'minimum': arr[0], 'length': len(arr)}
    for i in arr:
        if dictionary['maximum'] > i:
            dictionary['maximum'] = i
        if dictionary['minimum'] < i:
            dictionary['minimum'] = i
        dictionary['sumTotal'] += i
        dictionary['average'] = dictionary['sumTotal']/len(arr)

    return dictionary


analysis = ultimate_analysis([-1, 2, 1, -9])
print(analysis)

#  9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


def reverse_list(arr):
    for i in range(0, len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr


print(reverse_list([1, 2, 3, 4]))
print(reverse_list([37, 2, 1, -9, 7]))
