#import lib
#define variables
#take user input
#if else block
#print output
a=int(input("enter first num:"))
b=int(input("enter second num:"))
c=int(input("enter third num:"))
if a>=b and a>=c:
    print(f"{a} is the largest number")
elif b>=a and b>=c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")
