class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        for i, x in enumerate(nums):
            if (i != 0):
                if(x < nums[i-1]):
                    inc = False
                if(x > nums[i-1]):
                    dec = False
        return dec or inc


        
