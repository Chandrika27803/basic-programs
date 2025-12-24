#import lib
#define variables
sum=0
#take user input
#while loop
while True:
   n=input("enter the number:")
   if not n.isdigit():
        break
   else:
        sum+=int(n) 
#print output
print(sum)
