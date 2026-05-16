# 49 字母异位词分组
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vocab = {}
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            key = tuple(count)  # 重点
            if key not in vocab:
                vocab[key] = []
            vocab[key].append(s)
        return list(vocab.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))


l1 = [1, 3, 1]
l2 = [2, 3, 1]
assert id(l1) != id(l2)
assert id(tuple(l1)) == id(tuple(l2))
