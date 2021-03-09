def duplicate(var):

    index=0
    new=[]
    count=0
    while index<len(var):
        if a[index] not in new:
            new.append(a[index])
            count=count+1
        index=index+1
    print(count,new)
var=input("enter a str")
duplicate(var)
