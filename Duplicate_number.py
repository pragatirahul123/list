list = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
index=0
num=[]
while index<len(list):
        jar=index+1
        while jar<len(list):
            if list[index]== list[jar]:
                num.append(list[index])
                break
            jar=jar+1
        index=index+1      
print(num)
