class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moving_to = [0,0,0,0]
        for move in moves:
            if move == "U":
                moving_to[0]+=1
            elif move == "R":
                moving_to[1]+=1
            elif move == "D":
                moving_to[2]+=1
            else:
                moving_to[3] += 1
        return (moving_to[0] == moving_to[2]) and (moving_to[1] == moving_to[3])
        