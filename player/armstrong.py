num=int(input("enter the number"))
a = num
b = 0
while (num > 0):
    remainder = num % 10
    remainder = remainder**3
    num = num // 10
    b = remainder + b
print(b)
if(b==a):
    print("armstrong")
else:
    print("not armstrong")
