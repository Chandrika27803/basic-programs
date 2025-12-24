#import lib
#define function
# write condition
#take user input
#call the function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Division by zero error!!"
    else:
        return a/b
        
operator=input("enter the operator:")
a=int(input("enter a value:"))
b=int(input("enter b value:"))
if operator=="+":
    print("sum=",add(a,b))
elif operator=="-":
    print("diff=",sub(a,b))
elif operator=="*":
    print("mul=",mul(a,b))
elif operator=="/":
    print("div=",div(a,b))
else:
    print("invalid operator")



        
