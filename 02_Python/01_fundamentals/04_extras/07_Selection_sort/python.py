arr = [1,5,3,6,8,7,2,4]

def selection_sort(arr):
    for x in range(len(arr)):
        min_idx = x
        for i in range(x+1,len(arr)):
            if arr[min_idx] > arr[i]:
                min_idx = i
        arr[x], arr[min_idx] = arr[min_idx], arr[x]
    return arr




print(selection_sort(arr))