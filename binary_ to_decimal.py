list=[1,0,0,1,1,0,1,0,0,1,0,0]
var=len(list)-1
count=0
calculator=1
while var>=0:
    count=count + (list[var])*calculator
    calculator=calculator*2
    var=var-1
print(count)


