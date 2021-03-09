number = 30
list = [10, 11, 12, 13, 14, 17, 18, 19]
index=0
new=[]
while index<len(list):
    jar=index+1
    while jar<len(list):
        if list[index] + list[jar] == number:
            a1 = [list[i],list[jar]]
            new.append(a1)    
        jar=jar+1
    index=index+1
print(new)

