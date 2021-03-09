marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
index=0
while index<len(marks):
    jar=0
    sum=0
    while jar<len(marks[index]):
        sum=sum+marks[index][jar]
        jar=jar+1
    average=sum/len(marks[index])    
    index=index+1
    print(average)

