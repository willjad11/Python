#Update Values in Dictionaries and Lists
#Change the value 10 in x to 15. Once you're done, x should now be[[5, 2, 3], [15, 8, 9]].
#Change the last_name of the first student from 'Jordan' to 'Bryant'
#In the sports_directory, change 'Messi' to 'Andres'
#Change the value 20 in z to 30
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

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

print("----------NEXT CHALLENGE----------")

#Iterate Through a List of Dictionaries
#Create a function iterateDictionary(some_list) that, given a list of dictionaries,
#the function loops through each dictionary in the list and prints each key and the
#associated value. For example, given the following list.
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary(studentlist):
    for i in range(len(studentlist)):
        for key, value in studentlist[i].items():
            print(key + " - " + value + ",")

print(iterateDictionary(students))

print("----------NEXT CHALLENGE----------")

#Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries
#and a key name, the function prints the value stored in that key for each dictionary. For
#example, iterateDictionary2('first_name', students) should output:
#Michael
#John
#Mark
#KB
#And iterateDictionary2('last_name', students) should output:
#Jordan
#Rosales
#Guillen
#Tonel
def iterateDictionary2(keyname, somelist):
    for i in range(len(somelist)):
        if keyname in somelist[i].keys():
            print(somelist[i][keyname])

print("First names:")
iterateDictionary2('first_name', students)
print("Last names:")
iterateDictionary2('last_name', students)

print("----------NEXT CHALLENGE----------")

#Iterate Through a Dictionary with List Values
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints
#the name of each key along with the size of its list, and then prints the associated values within
#each key's list. For example:
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

def printInfo(anotherlist):
    key_list = list(anotherlist.keys())
    for i in range(len(key_list)):
        print(str(len(anotherlist[key_list[i]])) + " " + key_list[i].upper())
        for x in range(len(anotherlist[key_list[i]])):
            print(anotherlist[key_list[i]][x])

printInfo(dojo)
#Most confusing thing i've ever written lol