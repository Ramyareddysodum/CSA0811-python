x=int(input("Enter the number:"))
y=[]
count=0
for i in range(1,x+1):
    if x%i==0:
        y.append(i)
        count=count+1
print(count)
print(y)
f=int(input("Enter no.of factors:"))
for i in range(0,4):
    print(y[i])
    
