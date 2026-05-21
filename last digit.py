num=int(input("enter a number"))
last_digit=num%10
print("last_digit is:",last_digit)



num=int(input("ENTER A NUMBER:"))
removed=num//10
print("after removing a number:",removed)



num=int(input("enter a numer:"))
last_two=num%100
print("last_two digit are:",last_two)


num=int(input("enter a 5 digit number:"))
middle_digit=(num//100)%10
square=middle_digit** 2
print("square of",middle_digit,"is",square)



weight=int(input("enter weight in kg"))
height=int(input("enter height in cm"))
bmi=weight/((height/100)**2)
print ("bmi is:",bmi)


num=int(input("enter 4 digit number:"))
a=num //1000*1000
b=(num//100%10)*100
c=(num//10%10)*10
d=num%10
print(a,"+",b,"+",c,"+",d,"+")

radius=float(input("enter radius:"))
height=float(input("enter height:"))
volume= 3.14 * radius * radius * height
print("volume of a cylinder:",volume)


length=float(input("enter length:"))
breath=float(input("enter breath:"))
height=float(input("enter height:"))
volume=  length * breath
print("volume of cuboid:",volume)


cm=float(input("enter value in centimeters:"))
meter=cm/100
print("value in meters:",meter)"""


distance=float(input("enter distance:"))
time=float(input("enter time:"))
speed=distance/time
print("speed is:",speed)

