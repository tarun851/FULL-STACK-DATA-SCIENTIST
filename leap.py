y=int(input())
if y%4==0 and y%100!=0 :
    print("leap year")
elif y%400==0:
    print("leap year")
else:
    print("not a leap year")