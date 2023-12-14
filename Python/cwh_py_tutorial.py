# print("Hello World!") #to print a statement

# from playsound import playsound #to a play an audio file(mp3)
# playsound('D:\\Scam 1992 Ringtone(PaglaSongs).mp3')

# import os
# print(os.listdir()) #to print the directories of OS

# # 8)
# import random
# def play_game():
#     name = input("Hello, what's your name?\n")
#     print(f"Well, {name}, I am thinking of a number between 1 and 10.")
#     comp_guess, your_guess = 0,1
#     num_of_guesses = 0
#     comp_guess = random.randint(1,10)

#     while your_guess != comp_guess:
#         your_guess = int(input("Take a guess.\n"))
#         num_of_guesses += 1
#         if your_guess > comp_guess:
#             print("Your guess is too high.")
#         elif your_guess < comp_guess:
#             print("Your guess is too low.")
#         elif your_guess == comp_guess:
#             print(f"Good job, {name}! You guessed my number in {num_of_guesses} guesses!")
#             break

# play_game()


# # 3)
# import random
# print(random.randint(1,10))
# print(random.random())
# print(random.randrange(1,5))

# #Dictionary
# dict = {
#     'vijay': 'topper',
#     'virat': 'cricketer',
#     'vikas': 'daddu',
#     'marks': [1,2,3,65]
# }
# print(dict.keys()) #prints the keys of dictionary in dict_keys form
# print(list(dict.keys())) #prints the keys of dictionary in list form
# print(dict.values()) #prints the keys of dictionary in dict_values form
# print(list(dict.values())) #prints the keys of dictionary in list form
# print(dict.items()) #prints the (key,value) for all contents of dictionary in dict_items form
# updated_dict = {
#     'vj':'kacn',
#     'njc':'ahhcbj' 
# }
# dict.update(updated_dict) #updates the dictionary by adding key-value pairs from updated_dict
# print(dict['vj']) #prints value associated with 'vj'
# print(dict.get('vj')) #prints value associated with 'vj'
# # get() method is used to get rid of key error
# print(dict['vj2']) #returns an error as vj2 is not present in the 
# print(dict.get('vj2')) #returns None as vj2 is not present in the dict

# import time
# print()
# print(2021-((((time.time()/60)/60)/24)/30)/12)
# import random
# print(random.randint(1,2))

# str = input("Enter the string: ")
# substr = input("Enter the sub string: ")
# i = 0
# while substr in str:
#     str.replace(substr, "") 
#     i += 1
# print(i)
# print(str.count(substr))

# s = "iuhrnkJKSNjnsN"
# str = ""
# print(s)
# for char in s:
#     if char.islower():
#         str += char.upper()
#     else:
#         str += char.lower()
# print(str)

# def swap_case(s):
#     str = ""    
#     for char in s:
#         if char.islower():
#             str += char.upper()
#         else:
#             str += char.lower()
#     return str
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

# string = "vijay"
# l = list(string)
# l[2] = 'k'
# s = ''.join(l)
# print(s)

# class programmer:
#     company = "Microsoft"
#     def __init__(self, name, product):
#         self.name = name
#         self.product = product
#     def getInfo(self):
#         print(f"Name of {self.company} programmer is {self.name} and product is {self.product}.")

# harry = programmer("Harry", "Skype")
# alka = programmer("Alka", "Github")
# harry.getInfo()
# alka.getInfo()

# class Calculator:
#     def __init__(self, num):
#         self.number = num
#     def square(self):
#         print(f"The value of {self.number} square is {self.number**2}")
#     def squareRoot(self):
#         print(f"The value of {self.number} square root is {self.number**(1/2)}")
#     def cube(self):
#         print(f"The value of {self.number} cube is {self.number**3}")

# a = Calculator(5)
# a.square()
# a.squareRoot()
# a.cube()

# class sample:
#     a = "Harry"

# obj = sample()
# obj.a = "vicky"
# print(sample.a)
# print(obj.a)

# class greet:
#     @staticmethod
#     def greet():
#         print("Hola")

# damn = greet()
# damn.greet()

# class Train:
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats
#     def getstatus(self):
#         print(f"The name of the train is {self.name}")
#         print(f"The seats available in the train are {self.seats}")
#     def fareInfo(self):
#         print(f"The priec of the tickets is {self.fare}")
#     def bookTickets(self):
#         if(self.seats>0):
#             print(f"Your ticket has been booked, your ticket number is {self.seats}.")
#             self.seats -= 1
#         else:
#             print("Sorry, this train is full, kindly find tatkal.")        

# intercity = Train("Intercity Express: 14828", 90, 2)
# intercity.getstatus()
# intercity.fareInfo()
# intercity.bookTickets()
# intercity.bookTickets()
# intercity.bookTickets()
# intercity.getstatus()

# from typing import Mapping


# class replace:
#     def __init__(self,str,index,subStr):
#         self.str = str
#         self.index = index
#         self.subStr = subStr

#     def replace(self):
#         return self.str[:self.index]+self.subStr+self.str[self.index+1:]
#     # def bigshit(self):
#     #     return 5


# # replace("vijay",2,'k')

# print(replace("vijay",2,'k').replace())
# # b = shit()
# # print(a.bigshit())
# # print(shit().bigshit())
# # print(shit.bigshit(a))
# # a = [5,5,7,78]
# # a.sort()

# import random
# random.random()

# # 1)
# string = input()
# substring = input()
# count=0
# for i in range(len(substring),len(string)+1):
#     c=string[i-len(substring):i]
#     if(c==substring):
#         count+=1
# print(count)

# # 2)
# score = float(input("Enter the score: "))
# if score>=0 and score<=1:
#     if score>=0.9:
#         print('A')
#     elif score>=0.8:
#         print('B')
#     elif score>=0.7:
#         print('C')
#     elif score>=0.6:
#         print('D')
#     elif score<0.6:
#         print('E')
# else:
#     print("Entered score is out of range.")

# # 3)
# str = input().split()
# l = list()
# for i in str:
#     l.append(i.capitalize())
# for i in l:
#     print(i, end=' ')

# # alternative
# import string
# str = input()
# string.capwords(str)

# # 4)
# N = int(input())
# nums = input().split()
# l = list(map(int,nums))
# lRev = list()
# for i in range(N-1,-1,-1):
#     lRev.append(l[i])
# lSum = list()
# for i in range(N):
#     lSum.append(l[i]+lRev[i])
# for i in lSum:
#     print(i,end=' ')

# # 5)
# # enter N, V1 and V2 separarted by single space
# str = input().split()
# N = int(str[0])
# V1 = int(str[1]) # person velocity
# V2 = int(str[2]) # cab velocity
# t1 = N*(2**0.5)/V1 # time taken for person
# t2 = N*2/V2 # time taken for cab5
# if t1<t2:
#     print("Walk")
# else:
#     print("Cab")

# s = "vijay vardhan reddy"
# str = s.split()
# capStr = list()
# for i in str:
#     capStr.append(i.capitalize())

# for i in range(len(str)):
#     s = s.replace(str[i],capStr[i])
# print(s)


# # 6)
# N = int(input())
# lprime = list()
# for i in range(2,N):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         lprime.append(i)
# lsemiprime = set()
# for prime1 in lprime:
#     for prime2 in lprime:
#         if prime1*prime2<N and prime1!=prime2:
#             lsemiprime.add(prime1*prime2)
# sumOfSemiprime = False
# for semiprime1 in lsemiprime:
#     for semiprime2 in lsemiprime:
#         if semiprime1+semiprime2==N:
#             sumOfSemiprime = True
#             break 
# if sumOfSemiprime:
#     print("Yes")
# else:
#     print("No")

# # 6)
# def check_semiprime(x):
#     l=[]
#     for i in range(2,x):
#         if x%i==0:
#             l.append(i)
#     if len(l)==2 and l[0]!=l[1]:
#         for j in l:
#             for k in range(2,j):
#                 if j%k==0:
#                     return None       
#             else:
#                 return True

# def sum_semiprimes(n):
#     for i in range(1,(n//2)+1):
#         for j in range(n//2,n):
#             if i+j==n:
#                 a=check_semiprime(i)
#                 b=check_semiprime(j)
#                 if a==True and b==True:
#                     return True
                
# n=int(input("Enter a number:"))
# if n>200:
#     print("The number is too large")
# else:
#     s=sum_semiprimes(n)
#     if s==True:
#         print("YES")
#     else:
#         print("NO")string1='ABCDCDC'


# # 7)
# def is_vow(c):
#     return ((c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u'))
# str=input()
# print(str[0], end = "")
# for i in range(1,len(str)):
#     if ((is_vow(str[i - 1]) != True) or (is_vow(str[i]) != True)):
#         print(str[i], end = "")

# from itertools import combinations_with_replacement, combinations, permutations
# k = (0,1,2,3,4,5,6,7,8,9)
# r = 2
# l = tuple(combinations_with_replacement(k,r))
# L = set()
# for item in l:
#     L.add(tuple(permutations(item,r)))
# newL = list(L)
# for item in L:
#     for i in range(r):
#         newL.append(item[i])
# newL = list(newL)
# string = ''
# finalL = list()
# for i in newL:
#     for j in range(r):
#         string += str(i[j])
#     finalL.append(string)
#     string = ""
