a=int(input("enter first number:"))
b=int(input("enter second number:"))
operator=input("enter operator:")
if operator=="+":
    print("sum:",a+b)
elif operator=="-":
    print("sub:",a-b)
elif operator=="*":
    print("mul:",a*b)
elif operator=="/":
    if b==0:
        print("Division not possible!!")
    else:
        print("div:",a/b)
else:
    print("Invalid operator!!")
    
    
