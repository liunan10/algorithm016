def mergeSort(nums, begin, end):
    if begin >= end: return
    mid = begin + (end - begin) // 2
    mergeSort(nums, begin, mid)
    mergeSort(nums, mid + 1, end)
    merge(nums, begin, mid, end)

def merge(nums, begin, mid, end):

    i, j = begin, mid + 1
    cache = []
    while i <= mid and j <= end:
        if nums[i] < nums[j]:
            cache.append(nums[i])
            i += 1
        else:
            cache.append(nums[j])
            j += 1

    while i <= mid:
        cache.append(nums[i])
        i += 1
    while j <= end:
        cache.append(nums[j])
        j += 1
    nums[begin: end + 1] = cache

arr = [12, 11, 13, 5, 6, 7] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
mergeSort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
