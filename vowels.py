#import lib
#define variables
#take user input
#for block
#print output
s=input("enter the string:")
v=0
c=0
for i in s:
    if i in "aeiouAEIOU":
        v+=1
    else:
        c+=1
print(f"vowel count={v}")
print(f"consonant count={c}")
        
