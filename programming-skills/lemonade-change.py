class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0 
        tens = 0 
        twenties =0
        for x in bills:
            if x ==5:
                fives +=1
            elif x == 10:
                tens +=1
            else:
                twenties +=1 
            
            if x == 10:
                if fives <1:
                    return False
                else:
                    fives-=1
            elif x == 20:
                if tens >0 and fives>0:
                    tens -=1
                    fives -=1
                elif fives >=3:
                    fives -=3
                else:
                    return False
        return True


                
