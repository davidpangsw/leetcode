class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 0, 3, 5, 8, 10
        # 1, 3, 1, 4,  2
        # (10, 2) (8,  4)
        # (5, 1) (3, 3)
        # (0, 1)
        result = 0
        # leadPos, leadSpeed = float("inf"), float("inf")
        leadPos, leadSpeed = target, 1
        for pos, speed in sorted(zip(position, speed), reversed=True):
            # timeToCatchUp = (leadPos - pos) / (speed - leadSpeed) 
            # timeRemain = (target - leadPos) / (leadSpeed)
            # canCatchUp = (leadPos - pos) / (speed - leadSpeed) <= (target - leadPos) / (leadSpeed)

            if speed > leadSpeed and (leadPos - pos) / (speed - leadSpeed) <= (target - leadPos) / (leadSpeed):
                pass # join the fleet, ignore
            else:
                leadPos, leadSpeed = pos, speed
                result += 1
        return result

