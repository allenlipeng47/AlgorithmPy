import sys

class Solution(object):
    def findPeakElement1(self, nums):
        nums = [-sys.maxint] + nums + [sys.maxint]
        left, right = 1, len(nums) - 2
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1

    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right - 1: # this gurantees that there are always element on the left and right of mid element!!!
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left if nums[left] > nums[right] else right

s = Solution()
print (s.findPeakElement([1, 2, 3, 1]))