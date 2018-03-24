N=int(input("enter the number: "))
K=int(input("enter the number :"))
a=[]
sum=0
for i in range (N):
    l=int(input("enter the value"))
    a.append(l)
for i in range (K):
    sum=sum+a[i]
    print(sum)
