#import lib
#declare variables
sum=0
#take user input
n1=int(input("enter the starting number:"))
n2=int(input("enter the ending number:"))
#for loop
for i in range(n1,n2+1):
    sum=sum+i
#print output
print("sum=",sum)


