class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n - 1 not in num_set:
                curr = n
                cnt = 1
                while curr + 1 in num_set:
                    curr += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest