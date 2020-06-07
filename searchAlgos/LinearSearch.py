def  linear(list,search):
    for i in range(len(list)):
        if(search == list[i]):
            print(search, " found at : ",i)
            return True;
    return False

list = [20,12,-30,5,-1,8,35,-2]
found = linear(list,-2)
print(found)
