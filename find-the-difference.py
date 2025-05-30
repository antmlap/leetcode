class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
        sumt = 0
        sums = 0 
        for letter in s:
            sums += alphabet_dict.get(letter)
        for letter in t:
            sumt += alphabet_dict.get(letter)

        diff = sumt -sums 
        key = [k for k, v in alphabet_dict.items() if v == diff][0]
        return key

