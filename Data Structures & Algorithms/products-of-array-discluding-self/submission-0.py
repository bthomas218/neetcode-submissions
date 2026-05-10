class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        l = 1
        for num in nums:
            res.append(l)
            l *= num
        
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= r
            r *= nums[i]
        
        return res

