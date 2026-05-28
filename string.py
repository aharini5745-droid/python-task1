w="satisfied"
print(w.count("s"))



s=input("enter a name:\n")
count=0
for i in s:
    if i in "aeiou":
        count+=1
print("no.of.vowels found=",count)


a=("india is my country\n")
d=a.upper().split()
print(d)
for i in d:
    print(i)



w="universe"
print(w[::-1])

s=input("enter a name")
c=(s[::-1])
if s == c:
    print("palindrome")
else:
    print("not palindrome")


s="madam"
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")


s="india is my country"
b=s.split()
print(b)
for i in b:
    if len(i)>=7:
        print(i)
    
    
