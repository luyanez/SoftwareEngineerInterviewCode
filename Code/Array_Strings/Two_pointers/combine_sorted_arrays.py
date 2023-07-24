def comb_sorted_arr(arr1, arr2):
    pointer1 = 0
    pointer2 = 0
    res_pointer = []
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] < arr2[pointer2]:
            res_pointer.append(arr1[pointer1])
            pointer1 += 1
        elif arr1[pointer1] > arr2[pointer2]:
            res_pointer.append(arr2[pointer2])
            pointer2 += 1
        elif arr1[pointer1] == arr2[pointer2]:
            res_pointer.append(arr1[pointer1])
            pointer1 += 1
            pointer2 += 1

    if len(arr1)> len(arr2):
        while pointer1 < len(arr1):
            res_pointer.append(arr1[pointer1])
            pointer1 += 1
    elif len(arr2) > len(arr1):
        while pointer2 < len(arr2):
            res_pointer.append(arr2[pointer2])
            pointer2 += 1

    return res_pointer

arr1 = [1,5,7,9,10]
arr2 = [2,3,4,6,8,11,12]
res = comb_sorted_arr(arr1, arr2)
print("Final sorted array: ",res)
