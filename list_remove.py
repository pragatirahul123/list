list=[3,1,6,8,9,3,5,4,2]
num=int(input("enter a number"))
index=0
while index<len(list):
	if num==list[index]:
		list.remove(num)
	index=index+1
print(list)
