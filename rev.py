#import lib
#define variables
#take user input
#while block
#print output
n=int(input("enter a number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10 + digit
    n=n//10
print(f"reverse of n:{rev}")
