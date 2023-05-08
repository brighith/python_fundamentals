# 1 Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# 1.1 Change the value 10 in x to 15. Once you're done,
#  x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = "15"
print(x)
# 1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = "Bryant"
print(students)
# 1.3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
# 1.4 Change the value 20 in z to 30
z[0]['y'] = 30
print(z)
# ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
# 2 Iterate Through a List of Dictionaries
# should output: (it's okay if each val-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
students2 = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDicti(student2):
    stringReturn = ''
    for val in student2:
        stringReturn += (
            f"first_name - {val['first_name']}, last_name - {val['last_name']}\n")
    return stringReturn


print(iterateDicti(students2))
# ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ


# 3 Get Values From a List of Dictionaries


def iterateDicti2(val_name, some_list):
    stringReturn = ''
    for val in some_list:
        stringReturn += f"{val[val_name]} \n"
    return stringReturn


print(iterateDicti2('first_name', students2))
print(iterateDicti2('last_name', students2))

# ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
#  4 Iterate Through a Dicti with List Values
# Create a function printInfo(some_dict) that given a dicti whose values are all lists,
# prints the name of each val along with the size of its list,
#  and then prints the associated values within each val's list. For example:
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for val in some_dict:
        print(f"{len(some_dict[val])} {val.upper()}")
        for val in some_dict[val]:
            print(val)
        print("")


printInfo(dojo)
