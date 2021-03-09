list=[1,2,3,4,7,"a","s","c",3.1,5.4,1.2]
x=[]
y=[]
z=[]
for i in list:
	if type(i)==int:
		x.append(i)
	elif type(i)==float:
		y.append(i)
	elif type(i)==str:
		z.append(i)
print(x)
print(y)
print(z)



########################################################################################3


def change_num(list):
    x=[]
    y=[]
    z=[]
    for i in list:
        if type(i)==int:
            x.append(i)
        elif type(i)==float:
            y.append(i)
        elif type(i) == str:
            z.append(i)
    print(x)
    print(y)
    print(z)
change_num([1,2,3,"a","f","g",2.3,4.6,2.1])
    

