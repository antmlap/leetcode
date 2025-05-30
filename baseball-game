class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreList = [0]
        for i, operation in enumerate(operations):
            if operation == "+":
                scoreList.append(scoreList[-2] + scoreList[-1])
            elif operation == "D":
                scoreList.append(scoreList[-1] * 2)
            elif operation == "C":
                scoreList.remove(scoreList[-1])
            else:
                scoreList.append(int(operation))

        return sum(scoreList)


