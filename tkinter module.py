"""
from tkinter import *
root=tkinter.Tk()
w = Label(m, text='GeeksForGeeks.org!')
w.pack()
m.mainloop()

from tkinter import * #needed for Label but then tkinter.Tk() won't work
m=Tk()
w=Label(m,text='Hello World')
w.pack()
frame=Frame(m)#alternate is Frame(m).pack()
frame.pack()
def name_but(a):
    if a==1:
        print(f"I am {a}st button")
    elif a==2:
        print(f"I am{a}nd button")
    elif a==3:
        print(f"I am {a}rd button")
Button(m,text="Click me",activebackground="yellow",cursor="hand2",bg="blue",padx=5,pady=8,command=lambda:name_but(1)).pack()
Button(m,text="Click me",activebackground="yellow",cursor="hand2",bg="blue",padx=5,pady=8,command=lambda:name_but(2)).pack()
Button(m,text="Click me",activebackground="yellow",cursor="hand2",bg="blue",padx=5,pady=8,command=lambda:name_but(3)).pack()
m.mainloop()

#looping through tkinter button
from tkinter import *
root=Tk()
Frame(root,justify="center",width=400,height=400).pack()
def Text_display(lang):
    Text.delete(0,END)
    Text.insert(0,lang)
Text=Entry(root,width="30")
Text.pack()
button_dict={}
lang_list=['english','hindi','french','sanskrit','japanese']
for langu in lang_list:
    def action(lang=langu):
      return Text_display(lang)
button_dict[langu]=Button(root,text=langu,command=action)
button_dict[langu].pack(pady=10)

# Importing tkinter module 
from tkinter import *	

# Creating a tkinter window
root = Tk() 

# Initialize tkinter window with dimensions 300 x 250			 
root.geometry('300x250')	 

# Creating a Button
btn = Button(root, text = 'Click me !', command = root.destroy)

# Set the position of button to coordinate (100, 20)
btn.place(x=100, y=20)

root.mainloop()


#using config in button we can change any attribute used for it
#it is defined in a fucntion which is called upon by using command=name of function
from tkinter import *
root=Tk()
#root.geometry('300300')
def f(args):
    print(f"{args}")
photo=PhotoImage(file="")
btn=Button(root,image=photo,pady=30,padx=40,command=lambda:f('It works!'))
btn.pack()
root.mainloop()

import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x250")  # Set window size
root.title("Welcome to My App")  # Set window title

# Create a StringVar to associate with the label
#text_var = tk.StringVar()
#text_var.set("Hello, World!")

# Create the label widget with all options
label = tk.Label(root, 
                 text="Hello World",#variable=text_var,
                 anchor=tk.CENTER,       
                 bg="lightblue",      
                 height=3,              
                 width=30,              
                 bd=3,                  
                 font=("Arial", 16, "bold"), 
                 cursor="hand2",   
                 fg="red",             
                 padx=15,               
                 pady=15,                
                 justify=tk.CENTER,    
                 relief=tk.RAISED,     
                 #underline=0,           
                 wraplength=250         
                )

# Pack the label into the window
label.pack(pady=20)  # Add some padding to the top


# Run the main event loop
root.mainloop()

from tkinter import *
root=Tk()
l=Label(root,text="Hello World!",bg="yellow",font=("Arial","red"))
print(f"The text is{l.cget('text')},The bg color is {l.cget("bg")}")

# importing everything from tkinter
from tkinter import *

# creating the tkinter window
Main_window = Tk()

# variable
my_text = "Please Update"

# function define for 
# updating the my_label
# widget content
def counter():

	# use global variable
	global my_text
	my_text="GeeksforGeeks updated !!!"
	
	# configure
	my_label.config(text = my_text)

# create a button widget and attached 
# with counter function 
my_button = Button(Main_window,
				text = my_text,
				command = counter)

# create a Label widget
my_label = Label(Main_window,
				text = "geeksforgeeks")

# place the widgets 
# in the gui window
my_label.pack()
my_button.pack()

# Start the GUI 
Main_window.mainloop()

from tkinter import *

root = Tk()
n_entry = StringVar()
p_entry = StringVar()

def sub_fn():
    username = n_entry.get()
    password = p_entry.get()
    print(f"Username is={username}")
    print(f"Password is={password}")  
    n_entry.set("")
    p_entry.set("")

Label(root, text="Enter your credentials").grid(row=0, columnspan=2)
Label(root, text="Username").grid(row=1, column=0)
Entry(root, textvariable=n_entry).grid(row=1, column=1)
Label(root, text="Password").grid(row=2, column=0)
Entry(root, textvariable=p_entry, show="*").grid(row=2, column=1)
Button(root, text="Submit", command=sub_fn).grid(row=3, columnspan=2)
root.mainloop()

import tkinter as tk
def on_button_toggle():
    if var.get() == 1:
        print("Checkbutton is selected")
    else:
        print("Checkbutton is deselected")
root = tk.Tk()

# Creating a Checkbutton
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Enable Feature", variable=var, 
                             onvalue=1, offvalue=0, command=on_button_toggle)

# Setting options for the Checkbutton
checkbutton.config(bg="lightgrey", fg="blue", font=("Arial", 12), 
                   selectcolor="green", relief="raised", padx=10, pady=5)

# Adding a bitmap to the Checkbutton
checkbutton.config(bitmap="info", width=20, height=2)
# Placing the Checkbutton in the window
checkbutton.pack(padx=40, pady=40)
# Calling methods on the Checkbutton
checkbutton.flash()
root.mainloop()
"""
from tkinter import *
root=Tk()
#root.geometry(height=600,width=500)
result=StringVar()
result.set('')
screen=Entry(root,textvariable=result)
screen.pack()

def on_click(num):
    global result
    display=num
    if display=='=':
        try:
            if result.get().isdigit():
                 result.set(int(result.get()))
                 screen.update()
            else:
                  result.set(eval(screen.get()))
                  screen.update()
        except:
            result.set('error')
            screen.update()
            #result.set('')

        
    elif display=='C':
        result.set('')
    else:
        result.set(result.get()+display)
        screen.update()

#result.set("")


b=Button(root,text="9",font="Lucida 20 bold",command=lambda:on_click('9'))
b.grid(row=0,column=0)
b=Button(root,text="8",font="Lucida 20 bold",command=lambda:on_click('8'))
b.grid(row=0,column=1)
b=Button(root,text="7",font="Lucida 20 bold",command=lambda:on_click('7'))
b.grid(row=0,column=2)
b=Button(root,text="+",font="Lucida 20 bold",command=lambda:on_click('+'))
b.grid(row=0,column=3)



b=Button(root,text="6",font="Lucida 20 bold",command=lambda:on_click('6'))
b.grid(row=1,column=0)
b=Button(root,text="5",font="Lucida 20 bold",command=lambda:on_click('5'))
b.grid(row=1,column=1)
b=Button(root,text="4",font="Lucida 20 bold",command=lambda:on_click('4'))
b.grid(row=1,column=2)
b=Button(root,text="-",font="Lucida 20 bold",command=lambda:on_click('-'))
b.grid(row=1,column=3)


b=Button(root,text="3",font="Lucida 20 bold",command=lambda:on_click('3'))
b.grid(row=2,column=0)
b=Button(root,text="2",font="Lucida 20 bold",command=lambda:on_click('2'))
b.grid(row=2,column=1)
b=Button(root,text="1",font="Lucida 20 bold",command=lambda:on_click('1'))
b.grid(row=2,column=2)
b=Button(root,text="*",font="Lucida 20 bold",command=lambda:on_click('*'))
b.grid(row=2,column=3)


b=Button(root,text="C",font="Lucida 20 bold",command=lambda:on_click('C'))
b.grid(row=3,column=0)
b=Button(root,text="0",font="Lucida 20 bold",command=lambda:on_click('0'))
b.grid(row=3,column=1)
b=Button(root,text="=",font="Lucida 20 bold",command=lambda:on_click('='))
b.grid(row=3,column=2)
b=Button(root,text="/",font="Lucida 20 bold",command=lambda:on_click('/'))
b.grid(row=3,column=3)


root.mainloop()
"""
from tkinter import *

root = Tk() 
root.geometry("300x200") 

w = Label(root, text ='GeeksForGeeks', font = "50") 
w.pack() 

Checkbutton1 = IntVar() 
Checkbutton2 = IntVar() 
Checkbutton3 = IntVar() 

Button1 = Checkbutton(root, text = "Tutorial", 
                    variable = Checkbutton1, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10) 

Button2 = Checkbutton(root, text = "Student", 
                    variable = Checkbutton2, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10) 

Button3 = Checkbutton(root, text = "Courses", 
                    variable = Checkbutton3, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 10) 
    
Button1.pack() 
Button2.pack() 
Button3.pack() 

root.mainloop() 

from tkinter import *
root=Tk()
v=StringVar()
values={"RadioButton 1" :"1",
        "RadioButton 2" :"2",
        "RadioButton 3" :"3",
        "RadioButton 4" :"4"}

from tkinter import *

root = Tk()
# root.geometry("500x600")

result = StringVar()
result.set('')  # Initialize StringVar properly

screen = Entry(root, textvariable=result, font="Lucida 20 bold", bd=10, insertwidth=4, width=14, borderwidth=4)
screen.pack(pady=10)

def on_click(num):
    global result
    display = num
    if display == '=':
        try:
            if result.get().isdigit():
                result.set(int(result.get()))
            else:
                result.set(eval(result.get()))
        except:
            result.set('error')
    elif display == 'C':
        result.set('')
    else:
        result.set(result.get() + display)

# First row of buttons
f = Frame(root, pady=10, padx=20)
f.pack()

b = Button(f, text="9", font="Lucida 20 bold", command=lambda: on_click('9'))
b.grid(row=0, column=0)
b = Button(f, text="8", font="Lucida 20 bold", command=lambda: on_click('8'))
b.grid(row=0, column=1)
b = Button(f, text="7", font="Lucida 20 bold", command=lambda: on_click('7'))
b.grid(row=0, column=2)
b = Button(f, text="+", font="Lucida 20 bold", command=lambda: on_click('+'))
b.grid(row=0, column=3)

# Second row of buttons
f = Frame(root, pady=10, padx=20)
f.pack()

b = Button(f, text="6", font="Lucida 20 bold", command=lambda: on_click('6'))
b.grid(row=0, column=0)
b = Button(f, text="5", font="Lucida 20 bold", command=lambda: on_click('5'))
b.grid(row=0, column=1)
b = Button(f, text="4", font="Lucida 20 bold", command=lambda: on_click('4'))
b.grid(row=0, column=2)
b = Button(f, text="-", font="Lucida 20 bold", command=lambda: on_click('-'))
b.grid(row=0, column=3)

# Third row of buttons
f = Frame(root, pady=10, padx=20)
f.pack()

b = Button(f, text="3", font="Lucida 20 bold", command=lambda: on_click('3'))
b.grid(row=0, column=0)
b = Button(f, text="2", font="Lucida 20 bold", command=lambda: on_click('2'))
b.grid(row=0, column=1)
b = Button(f, text="1", font="Lucida 20 bold", command=lambda: on_click('1'))
b.grid(row=0, column=2)
b = Button(f, text="*", font="Lucida 20 bold", command=lambda: on_click('*'))
b.grid(row=0, column=3)

# Fourth row of buttons
f = Frame(root, pady=10, padx=20)
f.pack()

b = Button(f, text="C", font="Lucida 20 bold", command=lambda: on_click('C'))
b.grid(row=0, column=0)
b = Button(f, text="0", font="Lucida 20 bold", command=lambda: on_click('0'))
b.grid(row=0, column=1)
b = Button(f, text="=", font="Lucida 20 bold", command=lambda: on_click('='))
b.grid(row=0, column=2)
b = Button(f, text="/", font="Lucida 20 bold", command=lambda: on_click('/'))
b.grid(row=0, column=3)

root.mainloop()














def on_left_click(event):
    print("Left mouse button clicked at", event.x, event.y)

root = Tk()
root.title("Hello")
btn = Button(root, text="Click me")
btn.pack()

# Bind left mouse click event to the on_left_click function
btn.bind('<Button-1>', on_left_click)

root.mainloop()
#Making a simple calculator"""

""""""
