#question1
number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
number3=int(input("Enter third number:"))
average=((number1+number2+number3)/3)
print("The avg of three numbers is=",average)


#question2
inc=float(input("enter your gross income in dollars:"))
dep=int(input("Enter total dependents:" ))
income_tax=(inc-10000-(dep*3000))
final_tax=income_tax*0.2
final_tax=round(final_tax,2)
if final_tax<0: final_tax=0
else:final_tax=final_tax
print("your income tax is:",final_tax)


#questin3
sid=int(input("enter your SID;"))
name=str(input("enter your Name:"))
gender=input("enter your gender(M,F,U for unknown):")
course=str(input("enter course name:"))
cgpa=float(input("enter CGPA:"))
student=[sid,name,gender,course,cgpa]
print(student)






            

            
