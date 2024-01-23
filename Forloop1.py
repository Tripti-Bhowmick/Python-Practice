#print no between 1 to 10
for i in range(1,11):
 print(i,end=" ")
print("\n")

#print the sum of all no between 1 to 100
sum=0
for i in range(1,100):
 sum=sum+i
print(sum)
print("\n")

#find product of all elements in a list
list=[5,15,25,35,45,55]
product=1
for i in range(len(list)):
 product=product*list[i]
print(list)
print("product:",product)
print("\n")

#print all even no between 1 to 20

for i in range(1,21):
 if i % 2==0:
  print(i,end=" ")

print("\n")

#factorial
fact=1
n=int(input("Enter a no"))
if n==0:
 print(fact)
else:
 for i in range(1,n+1):
   fact=fact*i
 print(fact)
print("\n")

#largest no in a list
list=[8,3,13,11,17,16,18,10,4,7]
largest=list[0]
for i in range(len(list)):
  if list[i]>largest:
   largest=list[i]
print(largest)
print("\n")

#fibonacci sequence
n=int(input("Enter a no"))
a=0
b=1
print(a,b)
for i in range(2,n):
 x=a+b
 a=b
 b=x
 print(x)
print("\n")

#no of vowels in a given string
count=0
str2='aeiouAEIOU'
str=(input("enter a string:"))
for i in range(len(str)):
 if str[i] in str2:
  count+=1
print(count)
print("\n")

# multiplication table using loop
a=int(input("Enter 1st no:"))
n=int(input("enter the no of range:"))
for i in range(0,n):
 print(a,"*",i,"=",a*i)















 



