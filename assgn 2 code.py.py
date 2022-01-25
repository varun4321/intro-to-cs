#question1
String_1= "Pyhton is a case sensitive language"
print("(a) The length of the string is:", len(String_1))
print("(b) The reversed string is:",String_1[-1::-1])
String_2=String_1[10:26]
String_2.replace("a case sensitive","object oriented")
print("(e) The index of substring a is:",String_1.find("a"))
print("(f) The original string after removing whitespaces is:",String_1.replace("", ""))
print("\n")

#question3
a=56
b=10
#part a
print("part(a):",a&b)
#part b
print("part b:",a|b)
#part c
print("part c:",a^b)
#part d
print("part d:",a<<2,b<<2)
#part e
print("part e:",a>>2,b>>4)
print("\n")

#question2
name="Varun"
SID=21103069
dept_name="computer science"
Cgpa=9.9
print("Hey %s,"%name,"here!")
print("My SID is %d" %SID)
print("I am from %s"%dept_name,"and my CGPA is%f"%Cgpa)
print("\n")

#question4
numb_1=int(input("Enter your first no.:"))
numb_2=int(input("Enter your second no.:"))
numb_3=int(input("Enter your third no.:"))
if numb_1>numb_2 and numb_1>numb_3:
    print("the greatest number is:",numb_1)
elif numb_2>numb_1 and numb_2>numb_3:
    print("the greatest number is:",numb_2)
else: print("the greatest number is:",numb_3)
print("\n")

#question5
a=input("Enter the string:")
if "name" in a:
    print ("yes")
else:
 print ("No") 
print("\n")

#question6
leng_1=int(input("Enter 1st side length:"))
leng_2=int(input("Enter 2nd side length:"))
leng_3=int(input("Enter 3rd side length:"))
if leng_1 + leng_2 <= leng_3:
    print("No triangle cannot be formed")
elif leng_1 + leng_3 <= leng_2:
    print("No triangle cannot be formed")
elif leng_2 + leng_3 <= leng_1:
    print("No triangle cannot be formed")
else:
    print("Yes triangle can be formed")