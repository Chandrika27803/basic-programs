#import lib
#define variables
#take user input
#while block
#print output

# for number
n=int(input("enter a number:"))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10 + digit
    n=n//10
if temp==rev:
    print(f"{rev} is a palindrome number")
else:
    print(f"{rev} is not a palindrome number")

#for strings
s=input("enter the string:").replace(" ","").lower()
s1=s[::-1]
if s == s1:
    print(f"{s} is palindrome string")
else:
    print(f"{s} is not a palindrome string")

