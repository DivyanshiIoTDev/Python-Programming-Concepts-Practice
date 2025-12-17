# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:27:41 2025

@author: bishe


#reversing a string
s="Hello World"
a=s.split()
print(a)
b=s.split()[::-1] #The sliced string is reversed by[::-1]
#if reversed first then sliced then words will not be interchanged
d=s[::-1]
e=d.split()
print(e) #Output-['dlroW','olleH']
print(b)
c=" ".join(s.split()[::-1])
print(c)


#reversing a string with for loop
s="Geeks for coding"
a=s.split()
length=len(a)
b=[]
for i in range(length):
    b.append(a[length-i-1])
print(b)
"""
"""
#Reversing a string with recursion
def reverse_word(words):
    if not words:
        return ""
    return words[-1]+" "+reverse_word(words[:-1])
s="Geeks for Coding"
reverse_word="".join(reverse_word(s.split()))
print(reverse_word)


#Replacing any ith charachter
s="hello World"
s=s.replace("l","")
print(s)
print()
#method 2
s="hello World"
sa="".join(s.split("l"))
print(sa)
print()
#method3-using for loop
s="Hello World"
s="".join(i for i in s if i!='l')
print(s)

#Avoiding spaces
s='''Hello Geeks for geeks
                how are you 
                         you make me practice everyday 
                                          Thank you so much'''

#Uppercase Half String
s="helloworld"
s=s[:(len(s))//2].upper()+s[(len(s)//2):]
print(s)

#capitalize the first and last character of each word in a string
s='helloworld'
s=s[:1].upper()+s[1:len(s)-1]+s[len(s)-1:].upper()
print(s)

"""
#program to check if a string has at least one letter and one number


"""
a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):",a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)
    

r1 = 0 # range1
r2 = 10 #range2

li = [i.split(",") for i in range(r1, r2)]
print(li)

# Get user input for a nested list
user_input = [x.split(",") for x in input("Enter nested list (use commas and semicolons): ").split(";")]

print("Nested List:", user_input)

print(len(user_input))
"""



