#MID SEM 1 PRACTICE
#INPUTTING A MATRIX
"""
matrix = []
for i in range(5):
	# Append an empty sublist inside the list
	matrix.append([])
	for j in range(5):
		matrix[i].append(input("ENTER THE ELEMENTS OF ARRAY"))
print(matrix)
print("hello")

matrix = [["apple", "banana", "cherry"],
		["date", "fig", "grape"],
		["kiwi", "lemon", "mango"]]
print(matrix)

modified_matrix = []
for row in matrix:
	modified_row = []
	for element in row:
       modified_row.append(element.capitalize())
    modified_row.append(modified_row)
print(modified_matrix)

#Q4
list1=[]
list2=[]
list1='e!e!k!s!g'
list2='g!e!e!k!s'
a=list1.split("!")
b=list2.split("!")
if set(a)==set(b):
  print("They are same")
  print(set(a))
print(list(set(a)))
b=set('bjhskh jfksdhf ')
print(type(b))
print(b)

To remove duplicate items in a list,
the shortcut is convert it into set as set 
includes a charachter single time only.Convert it back into list

#Q1
a=input("Enter the date in this format dd-mm-yyyy")
a=a.replace("-","")

while int(a)>=9:
    sum=0
    for digit in a:
        sum+=int(digit)
        print(type(sum))
    a=str(sum)
print(sum)

#Q3
a=[[1,2],[1,3],[1,4],[1,5],[1,7],[2,7],[2,3],[4,5],[5,6],[6,7]]
c=3
for list in a:
    for item in list:
        if item==c:
       
a=str(3746)
print(list(a))

for j in range(2):
    l[j]=input("enter digit")
print(l)

#Reverse words in a sentence as well as each letter in the word
a=input("Enter a string")
a=' '.join(word[::-1]for word in a.split())
print(a)
print()

#Second largest term without sorting
def f(*args):
    a=list(map(int,args))
    k=a[0]
    for j in range(2):
        for i in range(len(a)):
            if a[i]>k:
                k=a[i]
        if j==1:
            break
        a.remove(k)
        k=a[0]
    return k
args=input("Enter numbers").split()
print("The second largets number is{}".format(f(*args)))

1. Lucky Word Finder
Write a Python program that takes a string as input and calculates its "lucky number." 
The lucky number is calculated by summing the ASCII values of all characters in the string. 
If the sum is greater than 9, repeatedly sum its digits until a single-digit number is obtained.

a=input("Enter a string")
sum=0
for char in a:
    sum+=ord(char)

while sum>9:
    num=0
    for digit in str(sum):
        num+=int(digit)
    sum=num

print(sum)


#printing all digits from units place methods
a=input("Enter a number")#need to join the reversed function is neccesary
a=''.join(reversed(a))
for char in a :
    print(char,end="")


#7. Find Palindromic Substrings
#Write a Python program to find all substrings of a given string that are palindromes.
def check_palindrome(str):
    if str[::-1]==str[::1]:
        return True
str=input("Enter a string")
for j in range():
    for i in range(j):
        if a

  
  #Rotating matrix by 90 degrees
list=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(input("Enter number"))
    list.append(row)
    
print(list)

#Remove duplicates from list
lst=input("Input a list")
lst=lst.split(',')
i=0
j=1
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[j]==lst[i]:
            lst.pop(j)
            j=j-1
print(lst)

lst = input("Input a list: ")
lst = lst.split(',')

i = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        if lst[j] == lst[i]:
            lst.pop(j)  # Remove the duplicate element
        else:
            j += 1  # Move to the next element
    i += 1  # Move to the next base element

print(lst)

#another method
lst=input("Input a list")
lst=lst.split(',')
new_list=[]
for element in lst:
    if element not in new_list:
        new_list.append(element)
print(new_list)

def check_palindrome(s):
    if s[ : ]==s[ : :-1]:
        return True
#check palindrome
str=input("Input a string")
if check_palindrome(str)==True:
    print("IT IS PALINDROME")
else:
    print("It is not palindrome")

#reversing a string
def rev_string(s):
    return s[::-1] 

str=input("input a string")
print(rev_string(str))

#finding substring
s=input("Input a string:")
sub=input("Input the substring")
if sub in s:
    print(sub)

#merging two lists in a dictionary one as key and other as value
d={}
list1=['tanu','is','the','best']
list2=['surbhi','is','only','good']
for key,element in zip(list1,list2):
    d[key]=element
print(d)
print(f"{list1}this is the list")

def find_max(args):
    k=args[0]
    for element in args:
        if element>k:
            k=element 
    return k

args=[2,3,45,67,32,90]
print(max(args))
print(f"The maximum value is {find_max(args)}")

#find factorial using recursion
def factorial_fn(n):

      return n*factorial_fn(n-1)
n=int(input("Input the number:")) 
print(factorial_fn(n))

t=()
t1=(1,2,3,4,5)
t2=(5,6,7,8)
t=t1+t2
print(t)

def factorial_fn(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_fn(n - 1)

# Get user input
n = int(input("Input the number: "))

# Calculate factorial
result = factorial_fn(n)

# Print the result
print(f"The factorial of {n} is {result}")


factorial=1
def factorial_fn(n):
    if n>0:
        global factorial
        factorial=factorial*n
        factorial_fn(n-1)
    return factorial
n=int(input("input a number:"))
result=factorial_fn(n)
print(result)    

dictu={}
dicti={1:'Tanu',2:'is',3:'the',4:'best'}
dicto={5:'Surbhi',6:'is',7:'only',8:'good'}
for keys,values in zip(dicti.keys(),dicto.values()):
    dictu[keys]=values
print(dictu)

dicti={1:'Tanu',2:'is',3:'the',4:'best'}
for key,value in dicti.items():
    print(f"{key}:{value}")

 #dictionary to store squares of numbers from 1 to 10
d={}
d={key:key**2 for key in range(1,11)}
print(d)

#recursive function to calculate the sum of the digits of a number
sum=0
def sum_fn(num):
    global sum
    if num>0:
       sum=sum+num%10
       sum_fn(int(num/10))
    return sum
 
num=int(input("Enter a number"))
result=sum_fn(num)
print(sum)

  #function that takes a dictionary as input and returns a new dictionary with keys and values swapped
d={}
for i in range(2):
    key=input("Input a key")
    value=input("Input a value")
    d[key]=value
dicti={}
for key,value in d.items():
    dicti[value]=key
print(dicti)

#create two lists:one with names and other with ages.Combine them into a dictionary where names are keys and ages are values
list1=['tanu','surbhi','divyanshi']
list2=[19,20,'pata nahin']
d={}
for element,item in zip(list1,list2):
    d[element]=item
print(d)
"""










    











     

     
