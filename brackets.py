#import lib
#define variables
#take user input
#print output
s=input("enter the brackets:")
c1=0
c2=0
c3=0
n=len(s)
for i in  range(n):
    if s[i]=="(":
        c1+=1
    elif s[i]==")":
        c1-=1
    elif s[i]=="[":
        c2+=1
    elif s[i]=="]":
        c2-=1
    elif s[i]=="{":
        c3+=1
    elif s[i]=="}":
        c3-=1
if c1==0 and c2==0 and c3==0:
    print("Brackets are balanced!!")
else:
    print("Brackets are not balanced!!")
        
