#Row

magic_square=[[8,3,4],
            [1,5,9],
            [6,7,2]]
        
index=0
while index<len(magic_square):
    jar=0
    sum=0
    while jar<len(magic_square):
        sum=sum+magic_square[index][jar]
        jar=jar+1
    index=index+1
    print(sum)
        




