'''num=int(input("enter a number:"))
if num% 2==0:
    print("even")
else:
    print("odd")


num=int(input("enter a number:"))
if num>0:
    print("positive")
if num<0:
    print("negative")
else:
    print("zero")



num=int(input("enter a number:"))
if num% 2==0 and num% 5==0:
    print("divisible by 2 and 5")
else:
    print("not divisible")

m=int(input("enter a number"))
if m>=500:
    print("A")
elif m>=450:
    print("B")
elif m>=300:
    print("C")
elif m>=250:
    print("D")
else:
    print("FAIL")


year=int(input("enter a year:\n"))
if year% 4!=0:
    print("leap year")
    if year% 100==0:
        print("leap year")
        if year% 400==0:
            print("leap  year")
else:
    print("not leap year")


for i in range(1,11,1):
    print(i)

for i in range(1,11,1):
    print(i*i)

for i in range(10,0,-1):
    print(i)

age=int(input("enter your age:"))
if age<=12:
    print("child")
elif age<=19:
    print("teen")
elif age<=30:
    print("adult")
else:
    print("senior")


num=int(input("enter a number:"))
cube=num**3
if cube>100:
    print("grater than 100")
else:
    print("below or equal to 100")


username=input("enter your name: ")
password=input("enter your password: ")
if username=="admin":
    print("username correct")
    if password=="5678":
        print("login successfull")
    else:
        print("wrong username")
else:
    print("wrong password")


ch=input("enter the ch:")
if ch in "AEIOUaeiou":
    print("vowel")
else:
    print("consonant")


n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=1
    print("sum=",sum)

for i in range(65,91):
    print (chr(i),end="")

n=int(input("enter number:"))
for i in range(1,11,1):
    print(i,"*",n,"=",i*n)'''





        




