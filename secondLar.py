#import lib
#define variables
#take user input
#print output
a=list(map(int,input("enter values with spaces:").split()))
n=len(a)
a.sort()
print(a[n-2])

#without sorting/with max func
a=list(map(int,input("enter values with spaces:").split()))
a=list(set(a))
f=max(a)
a.remove(f)
s=max(a)
print(s)

#without sorting/max func
a1=list(map(int,input("enter values with spaces:").split()))
a=0
b=0
for j in a1: #taking every element in list a1
    if j>a: #comparing each element is if greater than "a"
        a=j #if "j" is grater than "a" then assigned that value to "a"
#max value will be stored in "a"
for k in a1:#taking every element in list a1
    if a>k and b<k:# check if every element in list a1 is less than "a" and more than "b"
        b=k  #if "a" is grater than "k" and "b" is less than "k" then assigned that "k" value to "b"
#second max value will be stored in "b"
print(b)

