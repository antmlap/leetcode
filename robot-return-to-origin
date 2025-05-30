class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0 
        for letter in moves:
            if letter == "U":
                y += 1
            elif letter == "D":
                y -=1
            elif letter == "R":
                x +=1
            else:
                x -=1
        return y==0 and x == 0


