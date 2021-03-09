list=[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
index=0
new=[]
while index<len(list):
    a1=(list[0]+list[1])
    new.append(a1)
    index=index+1
    break
print(new)
