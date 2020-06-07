def  binary(list,search):
    start = 0
    end = len(list) - 1
    mid = (start + end)/2
    for i in range(len(list)):
        midInt = int(mid)
        print(start, midInt, end,list[midInt])
        if(list[midInt]==search):
            print(search, " found at ",midInt)
            return  True
        elif search<list[midInt]:
            end = midInt-1
        elif search>list[midInt]:
            start = midInt+1
        mid=(start+end)/2
        if mid==end or mid==start:
            return False
    return False

list = [-15,-5,-2,10,20,35,80,120]
found = binary(list,121 )
print(found)