#bubble sort for a list without in built functions
#16839245
#16839245
#16389245 -swap
#16389245
#16382945 - swap
#16382495 - swap
#16382459 - swap
'''In bubble sort the sorting algorithm moves as a bubble between adjacent entries
if nth element is greater than n+1th element, then the values are swapped'''
#time complexity - O(n2)

#function to do bubble sort
def bubble_sort(list):
    #find the length of the list
    list_len = len(list)
    #iterate until end of list - 1, to avoid list getting out of bound
    for i in range(0, list_len-1):
        for j in range(0,len(list) - 1):
            #print(j)
            if(list[j]>list[j+1]):
                list[j],list[j+1] = list[j+1],list[j]
        list_len = list_len-1
        print(list)
    return list


list = [20,12,-30,5,-1,8,35,-2]
bubble_sort(list)
print (list)
list = ["xr","br","zr","ar"]
bubble_sort(list)
print(list)