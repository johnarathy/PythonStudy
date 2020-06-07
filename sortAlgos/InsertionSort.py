#20,12,-30,5,-1,8,35,-2
#12,20,-30,5,-1,8,35,-2
#-30,12,20,5,-1,8,35,-2
#-30,5,12,20,-1,8,35,-2
#-30,-1,5,12,20,8,35,-2
#-30,-1,5,8,12,20,35,-2
#-30,-1,5,8,12,20,35,-2
#-30,-2,-1,5,12,20,8,35

def insertion_sort(list):
    for i in range(1,len(list)):
        temp = list[i]
        j=i-1
        while(j>=0 and temp<list[j]):
            list[j+1] = list[j]
            j=j-1
        list[j+1] = temp


list = [20,12,-30,5,-1,8,35,-2]
insertion_sort(list)
print (list)