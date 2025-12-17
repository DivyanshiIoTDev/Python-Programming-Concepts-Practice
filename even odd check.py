"""import sys

for line in sys.stdin:
    if 'q'==line.rstrip():
        break 
    print(f'Input:{line}') 
print("exit")
// 
print(int(5/5))
print(5/5)
class MyClass:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return MyClass(self.value and other.value)

a = MyClass(True)
b = MyClass(False)
c = a / b  # c.value is False
print(c.value)
//
a='geeksforgeeks'
for i in range(len(a)):
    print(a[i],end='')
       
        if a[i]=='e' or a[i]=='s':
         print(" ")
    i=i+1   
//
#to check even and odd
def evenodd_fn():
    x=int(input("Enter the integer="))
    if x%2==0:#converting to int is necessary as mathematical operators don't work for strings received from input by default
        print("it is even")
        
    else:
        print("it is odd")

 #check the status-conditional statement
try:
a=int(input("a="))
b=int(input("b="))
if a<0 or b<0:
    flag=False
    print(f"{flag}"5)
elif a>0 and b>0:
     flag=True
     print("%s"%flag)
else:
    print("no output")
except ValueError:
    print("invalid entry")
"""
def cat_hat(str):
  text="catinhat"
  if text.count("cat")==text.count("hat"):
    print(text.count("cat"))
    print("Both are present")
  else:
    print("both are not equal")
    print(text.count("hat"))
    print(text.count("cat"))
cat_hat(str)

def f():
 text = "geeks for geeks ."

# returns False
 result = text.endswith('for geeks')
 print (result)

# returns True
 result = text.endswith('geeks.')
 print (result)

# returns True
 result = text.endswith('for geeks .')
 print (result)

# returns True
 result = text.endswith('b geeks geeks geeks .')
 print (result)

 print(text.count("geeks",0,len(text))) 

f()

  