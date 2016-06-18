class Solution(object):
    def select(self, arr, k):
        return self.partition(arr, 0, len(arr) - 1, len(arr) - k)


    def partition(self, arr, low, high, k):
        if low > high:
            return -1
        l, h, pivot = low, high, arr[low]
        while l < h:
            while l < h and pivot <= arr[h]:
                h = h - 1
            arr[l] = arr[h]
            while l < h and pivot >= arr[l]:
                l = l + 1
            arr[h] = arr[l]
        arr[l] = pivot
        if l == k:
            return arr[l]
        elif l > k:
            return self.partition(arr, low, l - 1, k)
        else:
            return self.partition(arr, l + 1, high, k)

arr = [4, 3, 5, 2, 1]
s = Solution()
print (s.select(arr, 2))