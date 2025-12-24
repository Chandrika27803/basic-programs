def add(a,b=0):
    return a+b
    
#Main code starts here
print(add(3,4))
print(add(10))

#exceptions
#try executes first
#if an error is encountered the except will execute
#finally executes no matter what
try:
    n=int(input("enter a number:")) 
    print(100//n)
except ValueError:
    print("please enter a number")
except ZeroDivisionError:
    print("Division not possible")
finally:
    print("Done")
    
