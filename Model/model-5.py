def is_isomorphic(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        flag1,flag2={},{}
        for i in range(len(str1)):
         ch1,ch2=str1[i],str2[i]
         if ch1 not in flag1:
            flag1[ch1]=ch2
         print(flag1)
         if ch2 not in flag2:
            flag2[ch2]=ch1
         print(flag2)
         if flag1[ch1]!=ch2 or flag2[ch2]!=ch1:
            return False
    return True
str1=input("str1=")
str2=input("str2=")
print(is_isomorphic(str1,str2))

