list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
var=0
while var<len(list1):
    j=len(list2)-1
    while j>=0:
        print(list1[var],list2[j])
        var=var+1
        j=j-1

