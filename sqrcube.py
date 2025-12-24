#print squares of even numbers and cubes of odd numbers in the given range


#import lib
#define variables
#take user input
#print output
n1=int(input("enter the starting number:"))
n2=int(input("enter the ending number:"))
for i in range(n1,n2+1):
    if i%2==0:
        print(i**2)
    else:
        print(i**3)
