list = [5, 20, 15, 20, 25, 50, 20]
index=0
new=[]
while (index<len(list)):
    if list[index]==20:
        new.append(list[index])
        list.remove(list[index])
    index=index+1
print (list)
