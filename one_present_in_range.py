print("Enter the Start Range")
a=int(input())
print(a)
print("Enter the End Range")
b=int(input())
print(b)
c=0
for i in range(a,b+1):
    te=str(i)
    for j in te:
        if j=='1':
            c+=1
print("output",end=":")
print(c)