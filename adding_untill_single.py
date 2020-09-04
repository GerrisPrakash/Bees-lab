def ans(n):
    while n>=10:
        te=str(n)
        n=0
        for i in te:
            n+=int(i)    
    return n    
print("number : ",end="")
a=int(input())
print(a)
print("output : ",end="")
print(ans(a))