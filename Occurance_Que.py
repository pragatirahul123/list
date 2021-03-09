list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
index=0
new=[]
while index<len(list):
    count=0
    b=[]
    jar=0
    while jar < len(list):
        if list[index]==list[jar]:
            count=count+1
        jar=jar+1
    b.append(list[index])
    b.append(count)
    index=index+1
    if b not in new:
        new.append(b)
print(new,"times")
