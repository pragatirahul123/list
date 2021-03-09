list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
index=0
new=[]
while index<len(list1):
        if list1[index]  in list2:
            new.append(list1[index])
        index=index+1
print (new)
