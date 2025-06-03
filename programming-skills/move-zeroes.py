class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroCounter = 0 
        numCounter = 0 
        newList = [0] * len(nums)
        exists = False
        for num in nums:
            if num == 0:
                zeroCounter +=1
            else:
                newList[numCounter] = num
                numCounter += 1
            
        for x in range(zeroCounter):
            newList[-1 + -1 * x] = 0
        
        for i, num in enumerate(nums):
            nums[i] = newList[i]



                    
        
