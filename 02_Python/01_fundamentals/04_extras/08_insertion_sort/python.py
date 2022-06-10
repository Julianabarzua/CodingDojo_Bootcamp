
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]

        j= i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr


arr = [6,5,3,1,8,7,2,4]
print(insertion_sort(arr))



