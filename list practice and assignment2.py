# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:56:38 2025

@author: bishe

#List exercises

#matrix addition checking
def add_fn():
    rows=[]
    l3=[]
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            rows.append(l1[i][j]+l2[i][j])
    l3.append(rows)
    print(l3)
    
l1=[[1,2],[3,4],[4,5]]
l2=[[3,5],[7,3],[5,4]]
if len(l1)==len(l2):
        for i in range(len(l1)):
            if len(l1[i])!=len(l2[i]):
                if i==len(l1)-1:
                    i=i+1;
                break;
            print(i)
if i==len(l1)-1:
    print("equal-add")
    print(add_fn())
else:
    print("Don't add")
    

print("enter \" what 's up")
print("enter what's up")

def factorial_fn(n):
  if n==0 or n==1:
      return 1
  else:
      n=n*factorial_fn(n-1)
      return n
 
 #ASSIGNMENT 2     
factorial=int(input("Enter a number"))
print(factorial_fn(factorial))

def simple_interest(principal,rate,time):
    return (principal*rate*time)/100
def compound_interest(principal,rate,time):
    return principal * (1 + rate / 100) ** time - principal
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

print(f"Simple interest is{simple_interest(principal,rate,time)}")
print(f"Compound interest is{compound_interest(principal,rate,time)}")


#print all prime numbers in an interval
def isprime_fn(n):
    for i in range(2,(n//2)+1):
        if n%i!=0:
            return 1
        else:
            return 0
x=int(input("Enter upper limit"))
y=int(input("Enter lower limit"))
for n in range(y,x+1):
    isprime_fn(n)
    if isprime_fn(n)==1:
        print(n)
   
#fibonacci series
def if_fibonacci(n):
    i=0
    b=1 
    print(i)
    print(b)
    for m in range(1,n+1):
        i=i+b
        b=i
        print(i)
n=int(input("Enter a maximum range"))
if_fibonacci(n)

#Remove all duplicate charachter from a string
s=list(input("Enter a string"))
a=s[0]
for i in range(len(s)-1):
       if s[i]==a:
         s.pop(i)
print(f"{''.join(s)}")

s = list(input("Enter a string: "))
b=len(s)
for j in range(0,b):
   a=s[j]
   for i in range(b-1,j, -1):
       if s[i] == a:
          s.pop(i)
          b=len(s)

print(f"{''.join(s)}")

#list practice conitnue
"max of two numbers"

a=7
b=3 
print(max(a,b))
"""
#prime factorization method to find factorial


        

    
   


