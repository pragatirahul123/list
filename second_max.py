list1 = [10, 20, 4, 45, 99]  
index=0
max=0
second=0
while index<len(list1): 
    if list1[index]>max: 
        second=max
        max=list1[index] 
    elif list1[index]>second:
        max != list1[index]
        second=list1[index]
    index=index+1
 
print("second",second)
 
