arr=[1,2,4,6,3,7,8]

print("The missing numbers from ",end="")
print(min(arr),end=" ")
print("to",end=" ")
print(max(arr),end=" ")
print("is ",end="")
for i in range(min(arr),max(arr)+1):
    if i not in arr:
        print(i,end=" ")