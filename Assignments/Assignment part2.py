"""1.Write a code to reverse a number"""
# num=int(input("Enter number"))
# reversed_num=0
# while num!=0:
#     digit=num%10
#     reversed_num=reversed_num*10+digit
#     num//=10
# print("Reversed Number:" +str(reversed_num))
"""2.Write the code for Armstrong number"""
# num = int(input("Enter a number: "))
# # initialize sum
# sum = 0
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
"""3.Write code to check if the given string is pallindrome or not"""
# string=input("Enter string:")
# if(string==string[::-1]):
#    print("The string is a palindrome")
# else:
#    print("The string isn't a palindrome")
"""4.Write a code to check whether a given year is leap year or not"""
# year=int(input("Enter year to be checked:"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("The year is a leap year!")
# else:
#     print("The year isn't a leap year!")
"""5.Write code of greatest common divisor"""
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# i = 1
# while(i <= num1 and i <= num2):
#   if(num1 % i == 0 and num2 % i == 0):
#     gcd = i
#   i = i + 1
# print("GCD is", gcd)
import math
a= int(input("Enter 1st number: "))
b= int(input("Enter 2nd number: "))
print("HCF=: ",end="")
print(math.gcd(a,b))



"""6.Write a code to check if two strings are anagram or not"""
# str1 = "Race"
# str2 = "care"
# str1 = str1.lower()
# str2 = str2.lower()
# if(len(str1) == len(str2))
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)
#     if(sorted_str1 == sorted_str2):
#         print(str1 + " and " + str2 + " are anagram.")
#     else:
#         print(str1 + " and " + str2 + " are not anagram.")
# else:
#     print(str1 + " and " + str2 + " are not anagram.")
"""7.Write a code to calculate frequency of characters in a string"""
# str = "GOOGLE"
# dict = {}
# for i in str:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)
"""8.Write a code to check if two strings match where one string contains wildcard characters"""
"""9.Find non-repeating characters in a string"""
# a=input("Enter a string:")
# for i in a:
#   if(a.count(i)==1):
#     print(i,end=" ")
"""10.Write a code to find circular rotation of an array by K positions"""
"""11.Write a program to check whether a character is a vowel or consonant"""
# ch =input("Enter a character")
# if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
#     print(ch, "is a vowel")
# else:
#     print(ch, "is a consonant")