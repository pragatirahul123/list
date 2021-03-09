row=int(input("enter a row ="))
column=int(input("enter a column="))
index=1
a=1
empty=[]
while index<=column:
    empty1=[]
    b=a
    j=1
    while j<=row:
        empty1.append(b)
        j+=1
        b+=1
    empty.append(empty1)
    index+=1
    a+=column
print(empty)
