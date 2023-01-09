"""1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line."""
# num=[]
# for x in range(2000,3201):
#     if(x%7==0) and (x%5!=0):
#         num.append(str(x))
# print(','.join(num))

"""2.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary"""
# number = int(input("Type a number: "))
#
# numberDict = {}
# for i in range(1, number+1):
#     numberDict[i] = i*i
#
# print(numberDict)
"""3.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number"""
# numbers = input("Type in numbers seperated only by a comma :")
# numbers_split = numbers.split(',')
# number_tuple = tuple(numbers_split)
# print(number_tuple)
# print(numbers_split)
"""4.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.v"""
# row = int(input("Input number of rows: "))
# col= int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col)] for row in range(row)]
#
# for row in range(row):
#     for col in range(col):
#         multi_list[row][col]= row*col
#
# print(multi_list)
"""5.Write a program that calculates and prints the value according to the given formula:
 Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30"""
# import math
# numbers = input("Provide D: ")
# numbers = numbers.split(',')
# result_list = []
# for D in numbers:
#     Q = round(math.sqrt(2 * 50 * int(D) / 30))
#     result_list.append(Q)
# print(result_list)
"""6.Write a program that accepts a comma separated sequence of words as input and prints the words 
in a comma-separated sequence after sorting them alphabetically"""
# items = input("Input comma separated sequence of words")
# words = [word for word in items.split(",")]
# print(",".join(sorted(list(set(words)))))
"""7.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence."""
value = []
items=[x for x in input("Enter number").split(',')]
for p in items:
    y = int(p, 2)
    if y % 5==0:
        value.append(p)
print(','.join(value))
"""8.Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number"""
# values=[]
# for x in range(1000,3000):
#     s=str(x)
#     if (int(s[0]) %2 == 0) and (int(s[1]) %2 == 0) and (int(s[2]) %2 == 0) and (int(s[3]) %2 == 0):
#         values.append(s)
# print(",".join(values))