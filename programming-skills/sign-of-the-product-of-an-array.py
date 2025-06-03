class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sums = 1
        for x in nums:
            sums *= x 
        
        if sums >0:
            return 1
        elif sums < 0:
            return -1
        else:
            return 0 
