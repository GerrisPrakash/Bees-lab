print("Time :",end=" ")
time=input()
print(time)
h,m=map(int,time.split(":"))
ans=0
for i in range(h,int(m/5)):
    ans+=30
print("output",end=":")    
print(ans,end=" ")
print("degree")
