num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) #log statement access value from tuple
print(pizza_toppings[1]) #log statement access value from list
pizza_toppings.append('Mushrooms') #list add value to list
print(person['name']) #log statemnent access value from dictionary
person['name'] = 'George' #change value in dictionary
person['eye_color'] = 'blue' #change value in dictionary
print(fruit[2]) #access tuple value of index 2

if num1 > 45: #variable check, if statement
    print("It's greater") #log statement
else: #else statement
    print("It's lower") #log statement

if len(string) < 5: #variable check, if statement
    print("It's a short word!")  # log statement
elif len(string) > 15:  # else statement, variable check
    print("It's a long word!")  # log statement
else:  # else statement
    print("Just right!")  # log statement

for x in range(5): #for loop start
    print(x) # log statement
for x in range(2, 5):  # for loop start
    print(x)  # log statement
for x in range(2, 10, 3):  # for loop start, increment 3
    print(x)  # log statement
x = 0 #variable declaration 
while(x < 5): #while loop start
    print(x)  # log statement
    x += 1 #add 1 to variable

pizza_toppings.pop() #delete value from list
pizza_toppings.pop(1)  # delete value from list index 1

print(person)  # log statement
person.pop('eye_color') #delete value from dictionary
print(person)  # log statement

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #if statement
        continue
    print('After 1st if statement')  # log statement
    if topping == 'Olives': #if statement
        break

def print_hello_ten_times(): #function start
    for num in range(10): #for loop start
        print('Hello')  # log statement

print_hello_ten_times() #function call


def print_hello_x_times(x):  # function start
    for num in range(x):  # for loop start
        print('Hello')  # log statement


print_hello_x_times(4)  # function call


def print_hello_x_or_ten_times(x=10):  # function start
    for num in range(x):  # for loop start
        print('Hello')  # log statement


print_hello_x_or_ten_times()  # function call
print_hello_x_or_ten_times(4)  # function call


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)