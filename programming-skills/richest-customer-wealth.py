class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        initsum = 0 
        maximum = 0 
        for account in accounts:
            initsum = 0 
            for balance in account:
                initsum += balance
            maximum = max(maximum, initsum)
        return maximum
        
