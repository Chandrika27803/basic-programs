#import lib
#define variables
#take user input
#split the sentence
#count words and charcaters
#print output
s=input("enter the string:")
words=s.split()
c=0
print("word count=",len(words))
for word in words:
    if word:
        c+=len(word)
print("char count=",c)
    
