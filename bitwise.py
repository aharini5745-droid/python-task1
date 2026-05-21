'''#bitwise operator
a=10
b=5
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~(a&b))



bill=float(input("enter bill amount:\n"))
gst=18
total=bill+(bill*gst/100)
print("total amount:",total)


w1=float(input("enter a weight 1:\n"))
w2=float(input("enter a weight 2:\n"))
w3=float(input("enter a weight 3:\n"))
w4=float(input("enter a weight 4:\n"))
w5=float(input("enter a weight 5:\n"))
avg=(w1+w2+w3+w4+w5)/5
print("weight of average:",avg)


n=int(input("enter a number:"))
if(n&1)==0:
    print("even")
else:
    print("odd")


n=int(input("enter a number:\n"))
print("square:",n*n)


n=int(input("enter a number:\n"))
print("cube:",n*n)



x=5
y=10
x=x^y
y=x^y
x=x^y
print("after swapping")
print("x=",x)
print("y=",y)


a=int(input("enter frist number:"))
b=int(input("enter second number:"))
if a==b:
      print("equal")
else:
    print("not equal")

a=int(input("enter frist number:"))
b=int(input("enter second number:"))
if a>b:
      print("greater")
else:
    print("not greater")




n=int(input("enter a number:\n"))
if n<50:
      print("less than 50")
else:
    print("greater than or equal to 50")



a=int(input("enter frist number:"))
b=int(input("enter second number:"))
if a>b:
    print("a is lesser than b:")
elif a==b:
    print("a is equal to b:")
elif a<=b:
     print("b is greater than or equal to a:")
elif a*b:
      print("a is greater than or equal to b")
else:
    print("a is smaller than b")


a=int(input("enter frist value:\n"))
b=int(input("enter second value:\n"))
if a!=b:
    print("not equal")
else:
    print("equal")


l=[5,6,7,8]








n=int(input("enter a number:"))
if n in l:
      print("number exists")
else:
    print("not exists")


p=int(input("enter principle amount:"))
t=int(input("enter time:"))
r=int(input("enter rate:"))
ci=p*(1+r/100)**t
print("compound intrest:",ci)


a=[1,2,3,4,5]
n=int(input("enter a element:\n"))
if n in a:
      print("exists")
else:
    print("not exists")


a=100
b=100
print(a is b)

x=50
y=x
print(x is not y)

num=int(input("enter a number:\n"))
square=num*num
if str(square).endswith(str(num)):
    print(num,"is an automorphic number:")
else:
    print(num,"is not an automorphic number:")


num=int(input("enter a number:\n"))
if num%7==0:
    print(num,"is divisible by 7")
else:
    print(num,"is not divisible by 7")

ch=input("alphabets")
if ch>='A' and ch<='Z':
    print("first letter in upper_case",ch)
else:
    print("frist letter not in upper_case",ch)
    

    

    







