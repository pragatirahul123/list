user=int(input("enter a number"))
sum=0
var=user
while var>0:
    rem=var%10
    sum=sum+rem
    var=var//10
print(sum)
if(user%sum==0):
    print("Harshad number")
else:
    print("Not harshad number")
    
    
    
    
        
