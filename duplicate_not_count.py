list="apple"
index=0
new=[]
count=0
while index<len(list):
    if list[index] not in new:
        new.append(list[index])
        count=count+1
    index=index+1
print(count)
