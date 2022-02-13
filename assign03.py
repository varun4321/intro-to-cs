#Question 1
mystring=input("Give a string:")
list1=[]
list2=mystring.split()
l=len(list2)
a=dict()
t=dict()
if len(list2)==1:          
    for i in mystring:      
        list1.append(i) 
    for j in list1:        
        if j in a:         
            a[j]=a[j]+1   
        else:
            a[j]=1
    print(a)
print("Ques 1 Done")

#Question 2
month=int(input("Give month:"))

if(month in[1,3,5,7,8,10,12]):
    day=int(input("Give day:"))
    if(1<=day<=31):
        year=int(input("Give year:"))
        if(1800<=year<=2025):
            print("Date:",day,"/",month,"/",year)
            if(month==12 and day==31):
                print("Next Date:","1/1/",year+1)
            elif(day==31):
                print("Next Date:","1/",month+1,"/",year)
            else:
                print("Next Date:",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month in[4,6,9,11]):
    day=int(input("Give day:"))
    if(1<=day<=30):
        year=int(input("Give year:"))
        if(1800<=year<=2025):
            print("Date:",day,"/",month,"/",year)
            if(day==30):
                print("Next Date:","1/",month+1,"/",year)
            else:
                print("Next Date:",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month==2):
    year=int(input("Give year:"))
    if(1800<=year<=2025):
        day=int(input("Give day:"))
        if(year%4==0):
            if(1<=day<=29):
                print("Date:",day,"/",month,"/",year)
                if(day==29):
                    print("Next Date:","1/",month+1,"/",year)
                else:
                    print("Next Date:",day+1,"/",month,"/",year)              
            else:
                print("invalid day")
        else:
            if(1<=day<=28):
                print("Date:",day,"/",month,"/",year)
                if(day==28):
                    print("Next Date:","1/",month+1,"/",year)
                else:
                    print("Next Date:",day+1,"/",month,"/",year)       
            else:
                print("invalid day")     
    else:
        print("invalid year")
else:
    print("invalid month")
print("Ques 2 Done")    


#Question 3
mylist = [0,1,2,3,4,5,6,7,8,9,]
tupple_list = [] 
for value in mylist:
    tupple_list.append((value,value*value))     
print(tupple_list)
print("Ques 3 Done")
    
#Question 4
grade = int(input("Enter the grade:"))
lettergrade=" "
performance=" "

if grade == 10:
    lettergrade ="A+"
    performance = "Outstanding"
    print("Your Gradepoint is:",grade)
    print("Your Grade is",lettergrade,"and",performance,"Performance")
    
elif grade == 9:
    lettergrade ="A"
    performance = "Excelent"
    print("Your Gradepoint is:",grade)
    print("Your Grade is",lettergrade,"and",performance,"Performance")
    
elif grade == 8:
    lettergrade ="B+"
    performance = "Very Good"
    print("Your Gradepoint is:",grade)
    print("Your Grade is",lettergrade,"and",performance,"Performance")
    
elif grade == 7:
    lettergrade ="B"
    performance = "Good"
    print("Your Gradepoint is:",grade)
    print("Your Grade is",lettergrade,"and",performance,"Performance")
    
elif grade == 6:
    lettergrade ="C+"
    performance = "Average"
    print("your gradepoint is:",grade)
    print("Your Grade is",lettergrade,"and",performance,"Performance")
    
elif grade == 5:
    lettergrade ="C"
    performance = "Below Average"
    print("Your Gradepoint is:",grade)
    print("Your Grade is",lettergrade,"and",performance,"Performance")
    
elif grade == 4:
    lettergrade ="D"
    performance = "Poor"
    print("Your Gradepoint is:",grade)
    print("Your Grade is",lettergrade,"and",performance,"Performance")

else:
    print("Error!")
print("Ques 4 Done")    

#Question 5        
mystring = "ABCDEFGHIJK"
counter = 1
while (counter < 7):
    print(" "*(counter-1),mystring[0:11-((counter-1)*2)])
    counter += 1
print("Ques 5 Done")

#Question 6
mydict = dict()
myinput='Y'
while(myinput=="Y"):
    name=str(input("Enter Name:"))
    sid=int(input("Enter Sid:"))
    mydict[sid] = name
    myinput=input("Give Y to enter more sids in dictionary :")

print(mydict)    
#part(b)
partb={k: v for k, v in sorted(mydict.items(), key=lambda item: item[1])}
print(partb)
#part(c)
mylist = mydict.items()
sortedlist = sorted(mylist)
print(sortedlist)
#part(d)
entersid = int(input("Enter the SID : "))
print("The student with entered SID is")
print(mydict[entersid])
print("Ques 6 Done")

#Question 7
term_one = int(input("Give a number-"))
term_two = int(input("Give a number-"))
sum = term_one + term_two
series = [term_one,term_two]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Type y to continue and n to stop:")
print("The fibonacci series is")
print(series)

sum=0
for i in series:
    sum=sum+i
print("Average of the sequence")
print(sum/len(series))
print("Ques 7 Done")

#question 8
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
#part(a)
parta=set1.symmetric_difference(set2)
print(parta)
#part(b)
partb = set1^(set2^set3)
print(partb)
#part(c)
partc = (set1 & set2) | (set2 & set3) | (set3 & set1)
print(partc)
#part(d)
new_set={1,2,3,4,5,6,7,8,9,10}
partd=new_set-set1
print(partd)
#part(e)
parte=new_set-(set1|set2|set3)
print(parte)
print("FINISH")