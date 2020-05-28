def Sort(arr,start,end,target):
    mid=start+(end-start)//2
    if start>end:
        return -1
    if arr[mid]==target:
        return mid
    elif arr[start]<=arr[mid]:
        if target>=arr[start] and target<arr[mid]:
            return Sort(arr,start,mid-1,target)
        else:
            return Sort(arr,mid+1,end,target)
    else:
        if target>arr[mid] and target<=arr[end]:
            return Sort(arr,mid+1,end,target)
        else:
            return Sort(arr,start,mid-1,target)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == Sort(input_list,0,len(input_list)-1, number):
        print("Pass")
    else:
        print("Fail")
        

test_function([[], 6])  #test for empty array

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  #test for first element in array

test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 12], 12]) #test for last element in unrotated array

test_function([[6, 7, 8, 1, 2, 3, 4], 4])   #test for last element in rotated array

test_function([[6, 7, 8, 1, 2, 3, 4], 10])  #test for a element not in array