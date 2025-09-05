a=int(input("Enter the total number of classes:"))
b=int(input("Enter the total attended classes:"))
percentage=(b/a)*100
if(percentage>=75):
    print("the student is eligible to write exams with attendance:",percentage)
else:
    print("the is not eligible to write exams,attendance percentage:",percentage)    