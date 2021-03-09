list = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count=0
counter=0
sum=0
sum1=0
i=0
while i<len(list):
    if list[i]%2==0:
        sum=sum+list[i]
        count=count+1
        average=sum//count
        
    else:
        sum1=sum1+list[i]
        counter=counter+1
        average1=sum1//counter
    i=i+1
print("even number",average)
print("odd number",average1)
        
        
