#print list by taking dynamic input

#import lib
#define variables
#take user input
print("method 1")
a=list(map(str,input().split(",")))
print(a)

print("\nmethod 2")
a=[]
n=int(input("enter number of fruits:"))
for i in range(n):
    fruits=input("enter names of fruits:")
    a.append(fruits)
print("fruits:",a)

print("\nmethod 3")
a=input("enter fruits:")
fruits=a.split(',')
print(fruits)

#list comprehension
print("\nmethod 4")
items=[item for item in input("enter items separated by spaces:").split()]
print("your list is:",items)

