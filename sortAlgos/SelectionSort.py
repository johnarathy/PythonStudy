def selection_sort(list):
    min_pos = 0
    base_length = len(list)
    for j in range(min_pos,base_length):
        for i in range(0, len(list)):
            if(list[min_pos]<list[i]):
                list[min_pos],list[i] = list[i],list[min_pos]
        min_pos = min_pos+1
    return list

list = [20,12,-30,5,-1,8,35,-2]
selection_sort(list)
print (list)