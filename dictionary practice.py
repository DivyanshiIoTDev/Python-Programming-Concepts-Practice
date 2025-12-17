"""
d1={'x':1,'y':3}
d2={'y':3,'z':4}
for item in d1.keys():
    if item not in d2:
        d2[item]=d1[item]
print(d2)

#consider this dictionary {“Gfg”: “1:2:3”, “best”: “4:8:11”} then the output should be [{‘Gfg’: ‘1’, ‘best’: ‘4’}, {‘Gfg’: ‘2’, ‘best’: ‘8’}, {‘Gfg’: ‘3’, ‘best’: ’11’}].
d={"Gfg":"1:2:3", "best": "4:8:11"}

s_list=[]
f_list=[]
for values in d.values():
        s_list.append(values.split(':'))

#to find maximum number of terms in the list of dictionaries
length=0

length=max(len(item) for item in s_list)
i=0
for i in range(length):
    d1={}
    for key,element in zip(d.keys(),s_list):#USE of zip function for parallel running of key as well as value in a dictionary
        d1[key]=element[i]
    f_list.append(d1)
     
print(f_list)                         
print(s_list)
print(length)
"""

#using zip function for conversion of dictionary to list
# initial dictionary
data = {1:'Gaurav', 2: 'Sanket' , 3:  'Anjali' , 4:  'Priyanka'}

# Zip tuple of kays &amp; values into list
list_of_data = list(zip(data.keys(), data.values()))

# printing the resulting list
print(type(list_of_data))
print(list_of_data)






