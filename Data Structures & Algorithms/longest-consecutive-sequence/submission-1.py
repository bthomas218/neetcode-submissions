class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        res = 1

        for num in num_set:
            curr_num = num
            curr_seq = 1
            
            while curr_num + 1 in num_set:
                curr_seq += 1
                res = max(res, curr_seq)
                curr_num = curr_num + 1
            

        return res