# Bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

heights = [1,1,4,2,1,3]
bubble_sort(heights)
print(heights)