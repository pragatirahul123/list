list=[22,3,55,1,7,8]
i=0
max=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    i=i+1
print(max)

sec=0
j=0
while j<len(list):
    if max>list[j] and sec<list[j]:
        sec=list[j]
    j=j+1
print(sec)
