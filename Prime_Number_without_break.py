num=int(input("enetr a number"))
index=1
c1=0
while index<num:
    if num%index==0:
        c1=c1+2
    index=index+1
if (c1==2):
    print("prime number",num)
else:
    print("not prime number",num)
