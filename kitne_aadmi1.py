list = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count=0
counter=0
index=0
while index<len(list):
    if list[index]%2==0:
        count=count+1
        
    else:
        counter=counter+1
    index=index+1
print("even number",count)
print("odd number",counter)
        
        
    
