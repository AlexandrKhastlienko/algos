# Объединение отсортированных списков
class Solution(object):
    def __init__(self):
        self.result = []

    def merge(self, nums1, m, nums2, n):
        # укажу последний элемент
        i = m - 1
        j = n - 1
        k = m + n - 1

        # иду с конца вначало
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

        self.result = nums1

solution = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution.merge(nums1, m, nums2, n)

print(nums1)