"""
with open ('testfile.txt','a') as f:
    f.write("\nI am Divyanshi Singh")

import os,sys
if os.path.isfile('testfile.txt'):
    open('testfile.txt','r')
else:
    print("File does not exist")
    sys.exit()   

try:
    with open('testfile.txt','a') as f:
        f.write("It worked!")
        
finally:
    #print("NO FILE EXISTS")
    f.close()
    """







try:
    with open('textfile.txt','r')as f:
        org=f.read()
        org=''.join(org.split([::-1]))

    with open('testfile2.txt','w')as f1:
        f1.write('hello')
    
except FileNotFoundError:
    print("File not found")
    org=""
    
 

    



    


