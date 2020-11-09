def quickSort(nums, begin, end):
    if begin >= end: return
    pivot = partition(nums, begin, end)
    quickSort(nums, begin, pivot - 1)
    quickSort(nums, pivot + 1, end)

def partition(nums, begin, end):
    counter, pivot = begin, end
    for i in range(begin, end):
        if nums[i] < nums[pivot]:
            nums[i], nums[counter] = nums[counter], nums[i]
            counter += 1
    nums[counter], nums[pivot] = nums[pivot], nums[counter]
    return counter

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" %arr[i]),

quickSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i]),
