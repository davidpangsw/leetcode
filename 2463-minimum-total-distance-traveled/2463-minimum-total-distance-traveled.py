RESULT_MAX = float('inf')
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # sort the robots
        robot.sort()

        # clear factories and sort
        factory = [(fpos, flimit) for fpos, flimit in factory if flimit > 0]
        factory.sort()
        
        # mem[I][J] stores the minimum total distance for robot[0], ...robot[I] and factory[0], ... factory[J]
        # mem[I][J] only depends on mem[:I][J-1]
        mem = [[RESULT_MAX for _ in factory] for _ in robot]

        for J in range(len(factory)):
            for I in range(len(robot)):
                # print(f"To calculate mem[{I}][{J}]: ")
                # print(robot[:I+1])
                # print(factory[:J+1])
                result = RESULT_MAX
                total = 0

                # i, j = current robot, current factory
                j = J
                fpos, flimit = factory[j]
                for i in range(I, -1, -1):
                    if j < 0: # there are robots left, but no more factories
                        result = RESULT_MAX
                        total = RESULT_MAX
                        break
                    rpos = robot[i]

                    # conditions that robot[i] must take factory[j] :
                    # j == 0; or
                    # closer to the factory[j] than to factory[j-1] (outer or inner)
                    # mustTake = (j == 0) or (abs(fpos - rpos) <= abs(factory[j-1][0] - rpos))
                    if j > 0 and abs(fpos - rpos) > abs(factory[j-1][0] - rpos):
                        # If not a must-take, try the option that doesn't take factory[j]
                        # in this case, factory[j] must be removed (impossible to get better result if we keep it)
                        result = min(result, total + mem[i][j-1])
                        # print(f"robot[{i}] try not to take factory[{j}], {total + mem[i][j-1]}")

                    # robot[i] takes the factory[j]
                    total += abs(fpos - rpos)
                    flimit -= 1
                    # print(f"robot[{i}] takes factory[{j}], total={total}")

                    # if factory has no rooms
                    if flimit == 0:
                        j -= 1
                        fpos, flimit = factory[j] # j can be -1, simply ignore it (python allows it)
                        
                mem[I][J] = min(result, total)
                # print(f"mem[{I}][{J}] = {mem[I][J]}")
        return mem[-1][-1]
