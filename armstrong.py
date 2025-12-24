#import lib
#define variables
#take user input
#while block
#print output

n=int(input("enter a number:"))
temp=n
sum=0
l=len(str(n))
while n>0:
    digit=n%10
    a=digit**l
    sum+=a
    n=n//10
if temp==sum:
    print(f"{temp} is an armstrong number")
else:
    print(f"{temp} is not an armstrong number")
    
##armstong numbers in the given range
n1=int(input("Enter start number:"))
n2=int(input("Enter end number:"))
for i in range(n1,n2+1):
    temp=i
    sum=0
    l=len(str(i))
    while i>0:
        digit=i%10
        a=digit**l
        sum+=a
        i=i//10
    if temp==sum:
        print(f"{temp} is an armstrong number")
   
