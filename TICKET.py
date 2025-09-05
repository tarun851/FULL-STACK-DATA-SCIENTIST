price=int(input("Enter ticket price:"))
age=int(input("Enter age:"))
status=input("student(yes/no):")
totalprice=0
if(status=="yes" and age<=25):
    totalprice=price-price*0.2
    print("Final ticket price is:",totalprice)
elif(status=="no"):
    totalprice=price
    print("Final ticket price is:",totalprice)
elif(age>=60):
    totalprice=price-price*0.1
    print("Final ticket price is:",totalprice)
else:
    totalprice=price
    print("Final ticket price is:",totalprice)


