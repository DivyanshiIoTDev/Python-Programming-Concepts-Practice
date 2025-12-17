
# Python program to
# demonstrate init with
# inheritance
"""
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something


obj = B("Something")

from tkinter import *
root=Tk()
n_entry=StringVar()
p_entry=StringVar()
def sub_fn():
    username=n_entry.get()
    password=p_entry.get()
    print(f"Username is={username}")
    print(f"Username is={password}")
    n_entry.set("")
    p_entry.set("")

Label(root,text="Enter your credentials").grid(row=0,columnspan=2)
Label(root,text="Username").grid(row=1,column=0)
Entry(root,textvariable=n_entry).grid(row=1,column=1)
Label(root,text="Password").grid(row=2,column=0)
Entry(root,textvariable=p_entry,show="*").grid(row=2,column=1)
Button(root,text="Submit",command=sub_fn).grid(row=3,columnspan=2)

root.mainloop()

from tkinter import *

root = Tk()
n_entry = StringVar()
p_entry = StringVar()

def sub_fn():
    username = n_entry.get()
    password = p_entry.get()
    print(f"Username is={username}")
    print(f"Password is={password}")  # Fixed typo
    n_entry.set("")
    p_entry.set("")

# Header using grid
Label(root, text="Enter your credentials").grid(row=0, columnspan=2)

# Username
Label(root, text="Username").grid(row=1, column=0)
Entry(root, textvariable=n_entry).grid(row=1, column=1)

# Password
Label(root, text="Password").grid(row=2, column=0)
Entry(root, textvariable=p_entry, show="*").grid(row=2, column=1)

# Submit Button
Button(root, text="Submit", command=sub_fn).grid(row=3, columnspan=2)

root.mainloop()

# overriding in multilevel inheritance 

class Parent(): 
		
	# Parent's show method 
	def show(self): 
		print("Inside Parent") 
	
	
# Inherited or Sub class (Note Parent in bracket) 
class Child(Parent): 
		
	# Child's show method 
	def show(self):
		super().show() 
		print("Inside Child") 
	
# Inherited or Sub class (Note Child in bracket) 
class GrandChild(Child): 
		
	# Child's show method 
	def show(self): 
		super().show()
		print("Inside GrandChild")		 
	
# Driver code 
g = GrandChild() 
g.show() 
#g.display() 

class Student:
    def __init__(self,name,rollno,age):
        self.name=name
        self.rollno=rollno
        self.age=age
    
class Report(Student):
    def __init__(self,name,rollno,age,marks):
        super().__init__(name,rollno,age)
        self.marks=marks
        self.percentage=sum(marks)*100/400
        print(f"The name of the student is={self.name}\n" 
        f"The rollno is={self.rollno}\n "
        f"The age is={self.age}\n" 
        f"The percentage is={self.percentage}\n" 
        f"------------------------------------------")
    
    def __lt__(self,other):
        if self.percentage<other.percentage:
            return True
        else:
            return False
students= [
    Report("Alice", 101, 18, [85, 90, 78, 92]),
    Report("Bob", 102, 19, [75, 80, 85, 90]),
    Report("Charlie", 103, 20, [90, 92, 88, 95]),
    Report("Diana", 104, 18, [80, 85, 90, 75]),
    Report("Ethan", 105, 19, [70, 75, 80, 85]),
    Report("Fiona", 106, 20, [95, 90, 85, 80]),
    Report("George", 107, 18, [65, 70, 75, 80]),
    Report("Hannah", 108, 19, [88, 92, 85, 90]),
    Report("Ian", 109, 20, [78, 82, 88, 85]),
    Report("Jessica", 110, 18, [92, 95, 90, 88])
] 
for i in range(10-1):
    for j in range(10-i-1):
        if students[j] < students[j + 1]:
            students[j], students[j + 1] = students[j + 1], students[j]
for student in students:
    print(f"{student.name} (Roll No: {student.rollno}) - Percentage: {student.percentage:.2f}%")
    final_list=[]
for i in range(11):
    for j in range(10):
       if students[j]<students[j+1]:
           k=students[j+1]
       else:
           k=students[j]
    final_list.append(k)
print(f"The results are:{final_list}")



from PIL import Image,ImageFilter
with Image.open('imgprac.png')as img:
    gy=img.convert('L')
    scale='1'
    bw=gy.convert(scale)
    bw.show()
    blur_img=img.filter(ImageFilter.BLUR)
    blur_img.show()

#to check if a string is valid identifier or not

A valid identifier in Python is a name given to variables, functions, classes, or other objects, following specific rules:
It can contain letters (both uppercase and lowercase), digits (0–9), and underscores (_).

It must not start with a digit; it should start with a letter (A–Z, a–z) or an underscore (_).

It cannot be a Python keyword (like for, while, if, etc.).

It cannot contain spaces or special characters (like @, #, $, %, etc.).

Identifiers are case-sensitive (myVar and myvar are different).

Identifiers can be of any length.

Identifiers cannot consist only of digits.

lst_valid=[chr(i) for i in range(ord('A'),ord('Z')+1,1)]+['_']+[chr(i) for i in range(ord('a'),ord('z')+1,1)]
print(lst_valid)
final_list=lst_valid+[chr(i) for i in range(ord('1'),ord('9')+1,1)]
s=input("Input an identifier")
t=1
if s[0] in lst_valid:
            t=1
            for i in range(1,len(s)):
                    if s[i] in final_list:
                            t=1
                    else:
                            t=0
                            break   
            import keyword
            if s in keyword.kwlist:
                    t=0                
else:
            t=0
if t==1:
        print("Valid Identifier")
else:
        print("Not valid identifier")

 
name=['tanu','Divyanshi','dibu','tanna','surbhi']
branch=['CS','AEROSPACE','AIDS','IIOT','IIOT']
marks=['92','87','85','94','67']
list_students=[(name[i],branch[i],marks[i]) for i in range(5)]
branch_avg={}

for i in range(len(list_students)):
    if branch
    branch_avg[list_students[i][1]]=

k=list_students[0][1]
for i in range(list_students):
    if list_students[i][1]>k:
        k=list_students
        new_list.append(list_students[i],[1])
   

class Bank_Account:
    def __init__(self,account_number,balance=0):
        self.account_number=account_number
        self.balance=int(balance)
  
class Transaction(Bank_Account):
    def __init__(self,account_number,balance,amount):
        super().__init__(account_number,balance)
        self.amount=amount
    
    def withdrawal(self):
        try:
            self.amount=int(input("Enter the amount to be withdrawn"))
            if self.balance<=self.amount:
                print("Not enough balance")
            else:
                print(f"You have withdrawn {self.amount} rupees")
                self.balance=self.balance-self.amount
                print(f"Your updated balance is {self.balance}")
                Customer(self.account_number,self.balance,self.amount).print_details()
        except ValueError:
            print("Enter valid transaction")
        
    
    def deposit(self):
        try:
              self.amount=int(input("Enter the amount to be deposited"))
              print(f"You have deposited {self.amount} rupees")
              self.balance=self.balance+self.amount
              print(f"Your updated balance is {self.balance}")
              Customer(self.account_number,self.balance,self.amount).print_details()
        except ValueError:
              print("Enter valid transaction")

class Customer(Transaction):
    def __init__(Self,account_number,balance,amount):
        super().__init__(account_number,balance,amount)

    def print_details(self):
        print(f"Your account number is:{self.account_number}\n"
              f"Your balance is{self.balance}\n"
              f"Your recent transaction{self.amount}")
        
account_number=input("Enter account number")
response=input("PRESS W FOR WITHDRAWAL AND D FOR DEPOSIT")
if response=='W':
    Transaction(account_number,500,0).withdrawal()  
else:
    Transaction(account_number,500,0).deposit()
   
#wap to remove duplicates from a list without nested loops
lst=['44','87','hello','hellno','87','hello']
new_lst=[]

for i in range(len(lst)-1,-1,-1):
    if lst[i] in new_lst:
        lst.pop(i)
    else:
        new_lst.append(lst[i])

print(new_lst)

lst=[[1,2],[1,3],[1,4],[1,5],[1,7],[2,7],[2,3],[4,5],[5,6],[6,7]]
c=int(input("Enter the number"))
new_lst=[]
for i in range(len(lst)):
   
    if lst[i][0]==c:
       
        new_lst.append(lst[i][1])
        
    elif lst[i][1]==c:
        new_lst.append(lst[i][0])
compare_lst=[i for i in range(1,8)]
final_lst=[]
for element in new_lst:
    if element not in compare_lst:
        final_lst.append(element) 
print(final_lst)
print(new_lst)

from tkinter import *
r=Tk()
r.title('Counting Seconds')
button=Button(r, text='Stop', width=25, command=r.destroy)#r.destroy closes the screen
button.pack()

Label(r,text="ENTER NAME").grid(row=0)

e=Entry(r)
e.grid(row=0,column=1)
e.pack()


mainloop()

from tkinter import *

master = Tk()
button=Button(master, text='Stop', width=25, command=master.destroy)#r.destroy closes the screen

Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)

e2.grid(row=1, column=1)
Button.pack()
mainloop()

def Generate_seat_letters(number):
        seat_letters=[]
       
        lst=['A','B','C','D']
    
        rows=number//4
        for i in range(1,rows+1):
           for element in lst:
               seat_letters.append(f"{i}{element}")
        return seat_letters

def assign_seats(passenger,seat_letters):
    assigned={}
    for i in range(len(passenger)):
          assigned[passenger[i]]=seat_letters[i]
          #or use zip-->for person,seat in zip(passenger,seat_letters):
          # assigned[person]=seat 
          #run parallel for loop to assgn passenger name as key od dictionary and value as element in list seat_letters
    return assigned

number=int(input("Enter the total number of seats"))
print(f"{Generate_seat_letters(number)}")
passenger=['tanu','divya','surbhi','dibu','divyanjali']
print(assign_seats(passenger,Generate_seat_letters(number)))

class Vehicle:
    color='Red'
    def __init__(self,name,type,maxspeed,mileage):
        self.name=name
        self.type=type
        self.maxspeed=maxspeed
        self.mileage=mileage
        self.capacity=50
        self.fare=0
        
    def Seating_capacity(self,capacity):
        self.capacity=capacity
        return capacity
    def fare_calculation(self,fare):
        self.fare=fare
        self.fare=self.capacity*100

    def display(self):
        print(f"The name of the vehicle is{self.name}\n"
              f"The type:{self.type}\n"
              f"The color is {self.color}\n"
              f"The mileage is:{self.mileage}\n"
              f"The maxspeed is:{self.maxspeed}\n"
              f"The seating capacity is:{self.capacity}\n"
              f"The total fare is{self.fare}")

class Bus(Vehicle):
    def __init__(self,name,type,maxspeed,mileage):
        super().__init__(name,type,maxspeed,mileage)
        
    def Seating_capacity(self,capacity=50):
        self.capacity=capacity
        self.capacity=int(input("Enter the capacity"))
        return f"The capacity of the Bus is {self.capacity}"
    def fare_calculation(self,fare=0):
        self.fare=fare
        self.fare=self.capacity*110
        return self.fare
    def display(self):
        super().display()

class Car(Vehicle):
    def __init__(self,name,type,maxspeed,mileage):
        super().__init__(name,type,maxspeed,mileage)

        
    def Seating_capacity(self,capacity=50):
        self.capacity=capacity
        self.capacity=int(input("Enter the capacity"))
        return f"The capacity of the Car is {self.capacity}"
    
    def fare_calculation(self,fare=0):
        self.fare=fare
        self.fare=self.capacity*100
        return self.fare
    def display(self):
        super().display()

Vehicles=[Bus('Volvo','bigbus','180','150'),Car('Mahindra','Xylo','200','180')]
for vehicle in Vehicles:
    vehicle.Seating_capacity()
    vehicle.fare_calculation()
    vehicle.display()

class Project:
    def __init__(self,list_of_employees,project_id):
        self.list_of_employees=list_of_employees
        self.project_id=project_id
    
    def __add__(self,other):
       
        if len(self.list_of_employees)<len(other.list_of_employees):
            self.project_id=other.project_id
        self.list_of_employees=self.list_of_employees+other.list_of_employees

        return f"The new project is {self.project_id} with list of employees as {self.list_of_employees}"
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.list_of_employees=[]
    def __ge__(self,other):
        return self.id>=other.id #for ascending order
            



p1=Project(['tanu','divya'],'5')
p2=Project(['surbhi','divyanjali'],'4')
print(p1+p2)

list_of_employees=[Employee('tanu',2),Employee('divyanshi',5),Employee('surbhi',4),Employee('dibu',8)]
for i in range(len(list_of_employees)):
    for j in range(0,len(list_of_employees)-i-1):
        if list_of_employees[j+1]>=list_of_employees[j]:
            list_of_employees[j],list_of_employees[j+1]=list_of_employees[j+1],list_of_employees[j]
for employee in list_of_employees:
    print(f"{employee.name} (ID: {employee.id})")
    

with open("textfile.txt",'r') as f:
    content=f.read()
content=content.split(',')
d={}

for i in range(len(content)):
   count=0
   k=content[i]
   for j in range(i,len(content)):
       if content[j]==k:
          count=count+1
   d[k]=count

print(d)

with open("textfile.txt", 'r') as f:
    content = f.read()
print(content)
content = content.split(',')
d = {}

for i in range(len(content)):
    k = content[i]
    if k not in d:
        count = 0
        for j in range(len(content)):
         if content[j] == k:
            count += 1
        d[k]=count

print(d)

#GUI calculator
from tkinter import *
root=Tk()
display=StringVar()
display.set('')
screen=Entry(root,textvariable=display,font=('Lucida',30,'bold'),background='yellow')
screen.pack()
def on_click(t):
    if t=='=':
        try:
            if display.get().isdigit():
                display.set(int(display.get()))
                
            else:
                display.get(str(eval(display.get())))
                screen.update()
        except DivisionByZero:
            display.set('error')
    
    elif t=='C':
        display.set('')
        
    else:
        display.set(display.get()+t)
    
button=[['1','2','3','+'],
        ['4','5','6','-'],
        ['7','8','9','*'],
        ['C','0','=','/']]

print(len(button))
for i in range(len(button)):
    f=Frame(root)
    f.pack(side=BOTTOM)
    for j in range(4):
        m=button[i][j]
        b=Button(f,text=m,font="Lucida 20 bold",command=lambda x=m:on_click(x))
        #b.grid(row=i+1,column=j,padx=2,pady=2)
        b.pack(side=LEFT)
   
root.mainloop()

#Q-3
list_of_students=[('Divya','IIOT','96'),('Tanu','IT','97'),('Me','IIOT','94'),('Divyanshi','MC','93'),('Divyanjali','CS','92')]
d={}
for i in range(0,len(list_of_students)):
    k=list_of_students[i][1]
    if k not in d:
         d[k]=int(list_of_students[i][2])
         for j in range(i+1,len(list_of_students)):
            if list_of_students[j][1]==k:
                d[k]=d[k]+int(list_of_students[j][2])    
print(d)
#sort the branches in ascending order
for key,values in d.items():
    d[values]=key
sort_lst=[]
new_lst=[]
sort_lst=sorted(sort_lst.append([key for key in d]))
for element in sort_lst:
    if element in d:
        new_lst.append(d[key])
print(new_lst)

from tkinter import *

root = Tk()
display = StringVar()
display.set('')
screen = Entry(root, textvariable=display, font=('Lucida', 30, 'bold'), background='yellow')
screen.pack()

def on_click(t):
    if t == '=':
        try:
            # Evaluate the expression
            result = eval(display.get())
            display.set(result)
        except ZeroDivisionError:
            display.set('Division by zero')
        except Exception:
            display.set('error')
    elif t == 'C':
        display.set('')
    else:
        display.set(display.get() + t)

button = [['1', '2', '3', '+'],
          ['4', '5', '6', '-'],
          ['7', '8', '9', '*'],
          ['C', '0', '=', '/']]

for i in range(len(button)):
    f = Frame(root)
    f.pack(side=BOTTOM)
    for j in range(4):
        m = button[i][j]
        b = Button(f, text=m, font="Lucida 20 bold", command=lambda x=m: on_click(x))
        b.pack(side=LEFT)

root.mainloop()
"""










    




    

    


       




           



    
    
    


       




































    



    



