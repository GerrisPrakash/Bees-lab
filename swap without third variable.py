print("Enter x and y")
x=int(input())
y=int(input())
print("Before swapping")
print("x = ",end="")
print(x)
print("y = ",end="")
print(y)
print("After swapping without third variable")
x=x+y
y=x-y
x=x-y
print("x = ",end="")
print(x)
print("y = ",end="")
print(y)
