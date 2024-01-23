sum=0
for i in range(1,11):
 if i % 2==0:
  sum=sum+i
print(sum)
print("\n")

n=int(input("enter a no:"))
for i in range(1,n+1):
 for j in range(1,2*i):
  print("*",end=" ")
 print()
print("\n")

sum=0
i=1
n=10
while i<=10:
 sum=sum+i
 i+=1
print(sum)
print("\n")

#digit count
count=0
i=1
n=int(input("Enter the no:"))
while i<=n:
 count+=1
 n=n//10
print(count)
print("\n")

#reverse
rev=0
rem=0
n=int(input("enter the no"))
while(n>0):
 rem=n%10
 rev=(rev*10)+rem
 n=n//10
print(rev)
if rev==n:
 print("palindrome")
else:
 print("not palindrome")
print("\n")

#prime
import math
flag=False
i=0
n=int(input("enter the no"))
if(n==0 or n==1):
 flag=1
for i in range(2,int(math.sqrt)):
 if(n%i==0):
  flag=True
  break
if(flag==False):
 print("prime")
else:
 print("not prime")


 





 
