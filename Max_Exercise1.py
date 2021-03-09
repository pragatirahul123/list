a = [50, 40, 23, 70, 56, 12, 5, 100, 7]
index=0
max=0
while index<len(a):
    if a[index]>max:
        max= a[index]
    index=index+1
print(max)

