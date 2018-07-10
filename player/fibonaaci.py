n=int(input("enter the number:"))
n1=1
n2=1
count=0
for i in range(0,n):
  print(n1)
  nth=n1+n2
  n1=n2
  n2=nth
  count+=1
