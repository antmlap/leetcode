class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) < 3: 
            return 0
        
        for x in range(len(nums)-1, 1,-1):
            if(nums[x-2] + nums[x-1] > nums[x]):
                return nums[x-2] + nums[x-1] + nums[x]
        return 0 

