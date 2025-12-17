#LEETCODE PRACTICE
#Q-1 Given a string s,return the longest palindromic substring in s
"""
s=input("input a string")
for char in s:
    if 47<ord(char)<58 or 64<ord(char)<91 or 97<ord(char)<122 :
        continue;
    else:
        s=input("Enter a new valid string")
        
m=0
res=[]
a=[]
s=list(s)
for i in range(int(len(s)/2),0,-1):
    for j in range(0,i):
        if s[i-j]==s[i+j]:
            a=a.append(s[i+j])
        else:
            continue
    res[m]=str(a)
    m=m+1
      
k=res[0]
for element in res:
    if len(element)>len(k):
        k=element
print(k)"

#Solution

def is_palindrome(s):
    #Check if a string is a palindrome.
    return s == s[::-1]

def longest_palindromic_substring(s):
    #Find the longest palindromic substring in a string.
    # Validate input string
    while not s.isalnum():
        s = input("Enter a new valid string: ")

    max_length = 0
    longest_substring = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > max_length:
                max_length = len(substring)
                longest_substring = substring

    return longest_substring

# Get input string
s = input("Input a string: ")

# Find and print the longest palindromic substring
print(longest_palindromic_substring(s))


#Q-2Given an integer array nums of length n and an integer target,find three integers in nums such that the sum is closest to target.Return the sum of the three integers.You may assume that each input would have exactly one solution.

def sum_fn(a,b,c):
            if a+b+c==tgt or a+b+c==tgt-1 or a+b+c==tgt+1:
                   
                   global sum
                   sum=a+b+c
                   return True
            return False
                
            
                
sum=0

tgt=int(input("Enter a number"))
arr=input("Input a list")
arr=arr.split(',')
for i in range(len(arr)):
      for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                 # m=sum_fn(int(arr[i]),int(arr[j]),int(arr[k]))
                  #print(m)
                  if sum_fn(int(arr[i]),int(arr[j]),int(arr[k])):
                          print(sum)
                          print(f"The sum that is closest to the target is {sum}.({arr[i]}+{arr[j]}+{arr[k]}={sum})") 
            
                  else: 
                           print("Not found") 
  """
#longest word in dictionary
from PyDictionary 
import PyDictionary
dictionary = PyDictionary()
words=input("Input a list of words")
words=words.split(',')
new_word=''
for element in words:
    for char in element:
       
        if char not in new_word:
             new_word=char+new_word


        

       
    

    
      


                   
        
            
           
                
        



             
  

           

    























