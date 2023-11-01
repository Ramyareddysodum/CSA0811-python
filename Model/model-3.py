x=int(input("Enter the number:"))
y=[]
count=0
for i in range(1,x+1):
    if x%i==0:
        y.append(i)
        count+=1
print(count)
print(y)
z=int(input("Enter the nth factor:"))
for i in range(4,):
    print(y[3])
