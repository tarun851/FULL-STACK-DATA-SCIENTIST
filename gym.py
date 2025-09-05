mon1=500
mon6=2700
mon12=5000
a=int(input("Enter the membership period(1-5/6/12 months):"))
if(a<6):
    print("The cheaptest option is:",mon1*a)
elif(a==6):
    print("The cheaptest option is:",mon6)
elif(a==12):
    print("The cheaptest option is:",mon12)
else:
    print("invalid ")