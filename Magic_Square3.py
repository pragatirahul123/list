#Diagonal
magic_square=[[3,3,5],
             [1,1,1],
             [2,1,2]]
        

index=0
while index<len(magic_square):
    jar=0
    sum=0
    while jar<len(magic_square):
        sum=sum+magic_square[index][jar]
        jar=jar+1
        index=index+1
    print(sum)
        

        



