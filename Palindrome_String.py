b=input("enetr a string:")
rev=[]
index = len(b) 
while index > 0: 
    rev += b[ index - 1 ]
    index = index - 1 
#print(rev)
a=("".join(rev))
print (a)

if (a == b):
    print("palindrome ")
else:
    print("not palindrome")
    

 


##########################################################################################################################33   


b=input("enetr a string:")
i = len(b)-1
new=[]
while i >= 0:
    new.append(b[i])
    i = i - 1
print(new)
a=("".join(new))
print (a)

if (b == a ):
    print("palindrome ")
else:
    print("not palindrome")
    



 
