#跟merge template的区别：固定右边区间的值j，找到第一个满足条件的翻转对，因为左边已经排序好，可以计算出来大于j的翻转对的个数，同时找到左边比右边大的数，把右边放进cache。循环所有右边区间的元素。结束以后如果左区间还有数，放入cache.
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, begin, end):
        if begin >= end: return 0
        mid = begin + (end - begin) // 2
        count1 = self.mergeSort(nums, begin, mid)
        count2 = self.mergeSort(nums, mid + 1, end)
        mergeCount = self.merge(nums, begin, mid, end)
        count = count1 + count2 + mergeCount
        return count

    def merge(self, nums, begin, mid, end):
        i, k = begin, begin
        cache = []
        count = 0
        for j in range(mid + 1, end + 1):
            while i <= mid and nums[i] <= 2* nums[j]:
                    i += 1
            while k <= mid and nums[k] <= nums[j]:
                    cache.append(nums[k])
                    k += 1
            cache.append(nums[j])
            count += mid - i + 1
        while k <= mid:
            cache.append(nums[k])
            k += 1
        nums[begin: end + 1] = cache
        return count
