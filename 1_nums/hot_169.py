# 169 多数元素


# O(n) O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vocab = {}
        for i in nums:
            if i not in vocab:
                vocab[i] = 0
            vocab[i] += 1
        for n in vocab.keys():
            if vocab[n] >= len(nums) / 2.0:
                return n


# O(n) O(1) 删除任意两个不等的数字后，数组的众数不变
class Solution2(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate


# nums = [2, 2, 1, 1, 1, 2, 2]
nums = [2, 3, 1, 3, 0, 3, 3]
print(Solution2().majorityElement(nums))
