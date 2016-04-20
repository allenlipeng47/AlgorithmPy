class Solution(object):
    def twoSum(self, numbers, target):
        length = len(numbers)
        for i in xrange(length):
            search = target - numbers[i]
            left, right = 0, length - 1
            while left <= right:
                mid = left + (right - left) / 2
                if numbers[mid] < search:
                    left = mid + 1
                elif numbers[mid] > search:
                    right = mid - 1
                elif mid == i:
                    break
                else:
                    return (i, mid)
        return ()

s = Solution()
numbers = [-3, -1, 2, 3, 6, 8]
print (s.twoSum(numbers, 14))