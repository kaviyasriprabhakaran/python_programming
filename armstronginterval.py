a=int(input("enter the number: "))
b=int(input("enter the number: "))
for i in range(a,b):
    sum=0
    c=i
    while c>0:
        r = c % 10
        sum =sum + r **3
        c = c // 10
    if(i==sum):
                print(i)
