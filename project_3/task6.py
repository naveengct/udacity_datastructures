def get_min_max(arr=[]):
    if len(arr)==0:
        return None,None
    max=arr[0]
    min=arr[0]
    for i in range(1,len(arr)-1,2):
        if arr[i]<arr[i+1]:
            if arr[i+1]>max:
                max=arr[i+1]
            if arr[i]<min:
                min=arr[i]
        else:
            if arr[i]>max:
                max=arr[i]
            if arr[i+1]<min:
                min=arr[i+1]
    return min,max

import random
l = [i for i in range(0, 11)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print ("Pass" if ((0, 10) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 100)]  # a list containing 0 - 99
random.shuffle(l)
print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")