list=["durga","sadhavi","sonu","durga","sadhavi","vaibhav","sadhavi"]
index = 0
count = 0
counter=0
while index< len(list):
        if list[index]=="durga":
            count = count + 1
        elif list[index]=="sadhavi":
            counter=counter+1
                
        index = index + 1
print( "durga",count, "sadhavi",counter )
