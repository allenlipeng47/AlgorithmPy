class Solution(object):
    def partition(self, arr, low, high):
        if low >= high:
            return
        l, h, pivot = low, high, arr[low]
        while l < h:
            while l < h and pivot <= arr[h]:
                h = h - 1
            arr[l] = arr[h]
            while l < h and pivot >= arr[l]:
                l = l + 1
            arr[h] = arr[l]
        arr[l] = pivot
        self.partition(arr, low, l - 1)
        self.partition(arr, l + 1, high)

    def quickSort(self, arr):
        self.partition(arr, 0, len(arr) - 1)


arr = [4, 5, 3, 6, 2, 1]
s = Solution()
s.quickSort(arr)
print (arr)