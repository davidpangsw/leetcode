# Example:
# 0, 3, 5, 8, 10
# 1, 3, 1, 4,  2
# Fleet 1: (10, 2) (8,  4)
# Fleet 2: (5, 1) (3, 3)
# Fleet 3: (0, 1)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = 0
        leadPos, leadSpeed = float("inf"), float("inf")
        timeRemain = 0
        for pos, speed in sorted(zip(position, speed), reverse=True):
            # timeToCatchUp = (leadPos - pos) / (speed - leadSpeed) 
            # timeRemain = (target - leadPos) / (leadSpeed)
            # canCatchUp = (leadPos - pos) / (speed - leadSpeed) <= (target - leadPos) / (leadSpeed)
            if speed > leadSpeed and (leadPos - pos) / (speed - leadSpeed) <= timeRemain:
                pass # join the fleet, ignore
            else:
                # cannot join the fleet, become the lead of another fleet
                leadPos, leadSpeed = pos, speed
                timeRemain = (target - leadPos) / (leadSpeed)
                result += 1
        return result

