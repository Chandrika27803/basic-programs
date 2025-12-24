#import lib
#define variables
#take user input
#find common factor using euclidean algorithm
#Euclidean algorithm:->
#   rem=n1%n2 
#   replace n1=n2 & n2 = rem
#   continue until n2=0
#   n1=gcd
#print output
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
while n2!=0:
    r=n1%n2
    n1=n2
    n2=r
print(f"gcd={n1}")

