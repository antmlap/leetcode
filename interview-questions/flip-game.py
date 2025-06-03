class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        output = []
        currentState
        for i, letter in enumerate(currentState):
            if i != len(currentState) -1:
                if letter == "+" and currentState[i+1] == "+":
                    output.append(currentState[0:i] + "--" + currentState[i+2:])
        return output

