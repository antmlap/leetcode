class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        self.x = 0
        self.y = 0
        self.direction = 0 
        def moveForward():
            while self.direction < 0:
                self.direction += 360
            while self.direction >= 360:
                self.direction -= 360
            if self.direction ==0:
                self.y+=1
            elif self.direction == 90:
                self.x +=1
            elif self.direction == 180:
                self.y -=1
            elif self.direction == 270:
                self.x -=1 
            else:
                print("Error")
            
        for instruction in instructions:
            if instruction == "G":
                moveForward()
            elif instruction == "L":
                self.direction -= 90
            elif instruction == "R":
                self.direction +=90
            else:
                print("Error")
        return (self.x== 0 and self.y == 0) or self.direction % 360 != 0
        


