#import lib
#define variables
#take user input
#for loop
#compare ith element to every element
#if same increment the count
#print output
a=list(map(int,input("enter the elements:").split()))
n=len(a)
count=0
maxi=0
for i in range(n):
    newcount=0
    for j in range(n):
        if a[i]==a[j]:
            newcount+=1
    if newcount >count:
        maxi=a[i]
        count=newcount
print("most frequent element=",a[i])
print("count=",count)
       
