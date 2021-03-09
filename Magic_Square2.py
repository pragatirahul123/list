#Columun
magic_square=[[8,3,4],
            [1,5,1],
            [1,1,2]]
        
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square):
        sum=sum+magic_square[j][i]
        j=j+1
    i=i+1
    print(sum)
        



