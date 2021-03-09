list= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
index=0
count=0
counter=0
var=0
while index<len(list):
    if list[index]>=10000000:
        count=count+1
        
    elif(list[index]>=100000 ):
        counter=counter+1
    else:
        var=var+1
    index=index+1
        
print(" Crorepati hai",count)
print(" Lakhpati hai",counter)
print(" Dilwale hai",var)
        
