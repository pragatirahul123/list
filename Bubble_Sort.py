list=[8,15,1,9,3,10,4,7]
index=0
while index<len(list):
    jar=index+1
    while j<len(list):
        if list[index]>list[jar]:
           var=list[index]
           list[index]=list[jar]
           list[jar]=var
        jar=jar+1
    index=index+1
print(list)

 
