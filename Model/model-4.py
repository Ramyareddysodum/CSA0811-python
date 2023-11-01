str="We can play the game"
str=str.lower()
newstr=""
for i in range(0,len(str),1):
    if str[i] not in('a','e','i','o','u'):
        newstr+=str[i]
str=newstr
print(str)
        
