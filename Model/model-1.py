p=int(input("Enter principle amount:"))
t=int(input("Enter no.of years:"))
sc=input("Senior citizen:Yes/No")
G=input("Male/Female")
if sc is 'Y' and G is 'M':
    print("SI=",(p*t*12)/100)
elif sc is 'Y' and G is 'F':
    print("SI=",(p*t*15)/100)
else:
    print("SI=",(p*t*10)/100)
