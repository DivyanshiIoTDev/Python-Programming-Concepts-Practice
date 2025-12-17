"""
def push(S,item,top,MAX):
    if top==MAX-1:
        print("Overflow")
        for i in range(-1,top,1):
            print(S[i])
    else:
        top+=1
        S.append(item)
        return top
"""
def pop(S,top,MAX):
    if top==-1:
        return(-1,-1)
    else:
        temp=S[top]
        top-=1
        del S[-1]
        print(S[-1])
        print(f"{top}\n")
        for i in range(-2,top+1):
            print(f"{S[i]}\n")
           
        return (temp,top)
"""
def init():
    S=[]
    MAX=5
    top=-1
    return(S,MAX,top)
"""
S=[23,34,45,56,78]
MAX=5
top=4
pop(S,top,MAX)

"""
while(1):
    print('1:PUSH')
    print('2:POP')
    ch=int(input("Enter your choice"))
    if(ch==1):
        item=int(input("Enter item:"))
        top=push(S,item,top,MAX)
    elif(ch==2):
        if(top==-1):
            print("Underflow")
        else:
            pop(S,top,MAX)
    else:
        print("INCORRECT INPUT")

"""