#Countdown - Create a function that accepts a number as an input.
#Return a new list that counts down by one, from the number
#(as the 0th element) down to 0 (as the last element).
def countdown(num):
    for i in range(num, -1, -1):
        print(i)

countdown(10)

print("----------NEXT CHALLENGE----------")

#Print and Return - Create a function that will receive a list
#with two numbers. Print the first value and return the second.
def printreturn(list):
    print(list[0])
    return list[1]

print(printreturn([5,6]))

print("----------NEXT CHALLENGE----------")

#First Plus Length - Create a function that accepts a list and
#returns the sum of the first value in the list plus the list's length.
def firstpluslength(list):
    return list[0] + len(list)


print(firstpluslength([1,2,3,4,5]))

print("----------NEXT CHALLENGE----------")

#Values Greater than Second - Write a function that accepts a list and
#creates a new list containing only the values from the original list
#that are greater than its 2nd value. Print how many values this is and
#then return the new list. If the list has less than 2 elements, have
#the function return False.

def greaterthansecond(list):
    if len(list) < 3:
        return False
    else:
        newlist = []
        for i in range(len(list)):
            if list[i] > list[1]:
                newlist.append(list[i])
        print(len(newlist))
        return newlist

print(greaterthansecond([1,2,3,4,5]))

print("----------NEXT CHALLENGE----------")

#This Length, That Value - Write a function that accepts two integers as
#parameters: size and value. The function should create and return a list
#whose length is equal to the given size, and whose values are all the
#given value.
def thislengththatvalue(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list

print(thislengththatvalue(5,9))