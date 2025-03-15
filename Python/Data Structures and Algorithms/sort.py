# Bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


# merge sort  v1

# TC : O(nlogn)
# SC : O(n logn) as we are creating new arrays at each level of recursion 
# Note : we can optimize this to O(n) by using inplace merge sort - by using a temperory array of size n and using it to merge the arrays

def merge_sort(arr):
    n=len(arr)
    if n<2:
        return arr
    mid = n//2
    a1 = arr[:mid]
    a2 = arr[mid:]
    return merge(merge_sort(a1),merge_sort(a2))

def merge(arr1,arr2):
    n1= len(arr1)
    n2= len(arr2)
    i,j=0,0
    temp_arr = []
    while (i<n1 and j<n2):
        if arr1[i]<arr2[j]:
            temp_arr.append(arr1[i])
            i=i+1
        else:
            temp_arr.append(arr2[j])
            j=j+1
        
    while (i<n1):
        temp_arr.append(arr1[i])
        i=i+1
    while (j<n2):
        temp_arr.append(arr2[j])
        j=j+1
    
    return temp_arr


heights = [1,1,4,2,1,3]
print(heights)
merge_sort(heights)
print(merge_sort(heights))

