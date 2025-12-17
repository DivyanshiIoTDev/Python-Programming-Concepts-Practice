"""#python practice
#list comprehension
#dictionaries

a=[[1,2],[3,4],[5,6]]
res=[element for sublist in a for element in sublist]
print(res)


#using zip
#iterating through first elements of each list simultaneously
#use of zip function
for item1, item2, item3 in zip((1, 2, 3), ('a', 'b', 'c'), (True, False, True)):
	print(item1, item2, item3)
print("-----------")
a=[1,2,3]
b=['e','f','g']
c=['True','False','True']
for item1,item2,item3 in zip(a,b,c):
	print(item1,item2,item3)

res=[i for i in range(21) if i%2==0]
print(res)


s=input("Enter a sentence")
s=s.split()
res=[len(element)for element in s]
print(res)

res=[i**2 if i%2==0 else i**3 for i in range(11) ]  
print(res)

n = int(input("Enter the range"))
res = [(a, b) for a in range(n+1) for b in range(n+1) if (a + b) % 2 == 0]
print(res)

s=input("Enter a list in the format separated by ",")
s=s.split(',')
negative_label="negative"
positive_label="positive"
res=[(int(element),negative_label) if int(element)<0 else (int(element),positive_label) for element in s ]
print(res)

n=int(input("Enter the maximum value"))
res=[(i,1/i) for i in range(n+1) if i>0]
print(res)

s=input("Enter a sentence")
s=s.split()
vowels=['a','e','i','o','u']
res=[''.join(char for char in element if char not in vowels) for element in s]
print(res)

res=[i for i in range(1001) if i%7==0]
print(res)


res=[element for element in range(1001) for char in str(element) if char=='3']
print(res)"
"""