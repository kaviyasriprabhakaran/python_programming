a=int(input("enter the value"))
temp=a
rev=0
while(a>0):
    b=a%10
    rev=rev*10+b
    a=a//10
if(temp==rev):
    print("It is palindrome")
else:
    print("It is not palindrome")
