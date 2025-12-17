#linear search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return True
            
    return False
arr=input("Enter an array")
target=int(input("enter the target"))
arr=list(map(int,arr.split()))
if linear_search(arr,target)==True:
    print("it is found")
