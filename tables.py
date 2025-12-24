#import lib
#define variables
#take user input
n1=int(input("enter the starting number:"))
n2=int(input("enter the ending number:"))
#for loop
for i in range(n1,n2+1):
    for j in range(n1,n2+1):
#print output
        print(f"{i} * {j} = {i*j}")
    print()
