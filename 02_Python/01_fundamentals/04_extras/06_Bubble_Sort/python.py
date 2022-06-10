
arr = [1,5,3,6,8,7,2,4]


def Bubble_sort(arr):
    cont = len(arr)
    for x in range(cont):
        for i in range(len(arr)-1):
            if arr[i] > arr [i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        cont -=1
    return arr

print(Bubble_sort(arr))