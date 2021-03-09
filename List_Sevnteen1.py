colour1 = ["red", "orange", "green", "blue", "white"]
colour2 = ["black", "yellow", "green", "blue"]
new=[]
new2=[]
i=len(colour1)-1
while i>=0:
    j=0
    while j<len(colour2):
        if colour1[i]==colour2[j]:
            new.append(colour1[i])
            colour1.remove(colour1[i])
            new2.append(colour2[j])
            colour2.remove(colour2[j])
        j=j+1
    i=i-1
print(colour1)
print(colour2)
