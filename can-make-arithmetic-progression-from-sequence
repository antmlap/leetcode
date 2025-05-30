import math
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)   
        diff = arr[1]- arr[0]

        for i, x in enumerate(arr):
            if i !=0:
                if abs(x - arr[i-1]) != diff:
                    return False
    
        return True
