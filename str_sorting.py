list="nfsweohahdk"
index=0
new=[]
while index<len(list):
    new.append(list[index])
    index=index+1
jar=0
while jar<len(new):
    k=jar+1
    while k<len(new):
        if new[jar]>new[k]:
            var=new[jar]
            new[jar]=new[k]
            new[k]=var
        k=k+1
    jar=jar+1
print("".join(new))
