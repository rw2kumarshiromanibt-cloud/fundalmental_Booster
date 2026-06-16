'''syntax---'''
'''if condition:
    statement'''
'''a = 18
if a >= 16:
    print("True")'''

# age = 18
'''if age < 18:
    print("you can vote")'''
    
#print(10)
# print(20)

'''if condition:
    statement
else:
    statement'''

'''if age < 18:
    print("you can vote")
else:
    print("you can not vote")'''

'''age = int(input("Enter your age : "))
if age >= 18:
    print("you can vote")
else:
    print("you can not vote")'''

#marks = 40
# sports  = True
          

'''if marks < 40 or sports:
    print("You can eligible")
else:
    print("Not Eligible")'''


# 3 ladder

'''if condition:
    statement
elif : condition :
    statement
elif : condition :
    statement
else :
    statement'''


'''marks = int(input("Enter your marks : "))

if marks >= 90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >=60:
    print("Grade c")
else:
    print("Grade D")'''


# Short-hand Syntax or Ternary Statement

'''true_part if condition else fales part'''
    
'''if marks < 40 or sports:
    print("You can eligible")
else:
    print("Not Eligible")'''

'''marks = 50
sports = True

print("You can eligible") if marks < 40 or sports else print("Not Eligible")'''


# nested statement

'''a = int(input("enter 1st num :"))
b = int(input("enter 2nd num :"))
c = int(input("enter 3rd num :"))'''


'''if a > b:
    if a>c:
        print("a is max")
    else:
        print("c is max")
else :
    if b > c :
        print("b is max")
    else:
        print("c is max")'''


'''if a == b and b ==c:
    print("all are same")
else:
    if a > b:
        if a>c:
            print("a is max")
        else:
            print("c is max")
    else :
        if b > c :
            print("b is max")
        else:
            print("c is max")'''



# match case

'''a = int(input("enter num : "))

match a :
        case 1:
            print("Jan")
        case 2:
            print("Feb")
        case 3:
            print("Mar")
        case 4:
            print("Apr")
        case 5:
            print("May")
        case 6:
            print("June")
        case 7:
            print("july")
        case 8:
            print("Aug")
        case 9:
            print("Sep")
        case 10:
            print("Oct")
        case 11:
            print("Nov")
        case 12:
            print("Dec")
        case _:
            print("Invalid Month Number")'''



# while Loop
'''syntax :
        
initilization           # i = 1
while condition:
        body
        increment/decrement '''


#WAp to print 1 to 10:

                
'''i = 1
while i <= 10:
        print(i)
        i+=1'''

#WAp to print 10 to 1:

'''i = 10
while i >=1:
        print(i)
        i-=1'''

#Wap to print 1 to N.

'''N = int(input("Enter Number : "))
i = 1
while i <=N:
        print(i)
        i+=1'''

#WAP to print even number bte 1 to N.

'''N = int(input("Enter a Number : "))
i = 1
while i<=N:
        if i%2==0:
                print(i)
                
        i+=1'''

# WAP to find odd number btw 1 to N
'''N = int(input("Enter a Number : "))
i = 1
while i<=N:
        if i%2!=0:
                print(i)
                
        i+=1'''

# for Loop
'''syntax--
for variable in iterator/collection:
        body'''

'''for a in "python":
        print(a)'''

        
# range()
'''range([start],end,[step])
[start]-by default - 0(optional)
end - madetory
[step]-optional--by default - 1

range(10)
range(1,10)
range(1,10,2)'''

'''for i in range(1,11,2):
        print(i)'''

# Wap to print 10 to 1:

'''for i in range(10,0,-1):
        print(i)'''

'''for i in range(1,20):
        if i%2==0:
                print(i)'''

'''a = int(input("Enter a number :"))
b = int(input("Enter a number : "))
for i in range(a,b,5):
        if i%2==0:
                print(i)'''

# WAP to creata a table ...

'''a = int(input("Enter a number : "))

for i in range(1,11):
        b = a*i
        print(a,"*",i,"=",b)'''

# control Statement
#jump statement
''' break-to stop the iteration
continue - to skip iteration
pass - it is a placholder'''

'''i = 1
while i<=10:
        if i==5:
                continue
        print(i)
        i+=1'''


'''for i in range(1,10):
        if i==5:
                pass
               
        print(i)'''

# Nested Loop
'''n = int(input("Enter number : "))
for i in range(1,11):
        print(n,"*",i,"=",n*1)'''

'''n1= int(input("Enter a num : "))
n2 = int(input("Enter end num : "))

for n in range(n1,n2+1):
        for i in range(1,11):
                print(n,"*",i,"=",n*i)'''

# sqr pattern

'''for i in range(1,6):
        for j in range(1,5):
                print("*",end=" ")
        
        print()'''

'''for i in range(1,6):
        for j in range(i):
                print("*",end=" ")
        print()'''

'''for i in range(6,0,-1):
        for j in range(i):
                print("*",end=" ")
        print()'''

print("HEllo",end=" ")
print("AIML")

