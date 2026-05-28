'''for i in range(1,8):
    for j in range(i+1,8):
        print(" ", end="")
    for k in range(1,i):
        print("* ", end="")
    print()
for i in range(1,8):
    for m in range(1,i):
        print(" ", end="")
    for n in range(i+1,8):
        print("* ", end="")
    print()


n=int(input("enter a number:"))
t=n
sums=0
product=1
while t>0:
    d=t%10
    sums+=d
    product*=d
    t//=10
if sums==product:
    print("spy no")
else:
    print("not spy")




n=int(input("enter a number:"))
t=n
sums=0

while t>0:
    d=t%10
    sums+=d
    t//=10
if n%sums==0:
    print("harsed no")
else:
    print("not harshad")



n = int(input("Enter a number: "))
t = n
sums = 0
digits = len(str(n))

while t > 0:
    d = t % 10
    sums += d ** digits
    t = t // 10

if sums == n:
    print("Armstrong")
else:
    print("Not Armstrong")


n = int(input("Enter a number: "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c



num=int(input("enter a number:\n"))
square=num*num
if str(square).endswith(str(num)):
    print(num,"is an automorphic number:")
else:
    print(num,"is not an automorphic number:")'''



for i in range(1,6):
    for j in range(1,6):
        if j==5 and j==1:
            print("H","",end=" ")
        elif i==j and i<=6:
            print("H","",end=" ")
        elif i==3 and j==5:
            print("H","",end=" ")
        else:
            print("","",end=" ")
    print()
