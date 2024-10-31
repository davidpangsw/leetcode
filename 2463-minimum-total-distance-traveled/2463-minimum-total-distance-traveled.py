RESULT_MAX = float('inf')
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # sort the robots
        robot.sort()

        # clear factories and sort
        factory = [(fpos, flimit) for fpos, flimit in factory if flimit > 0]
        factory.sort()
        
        # mem[I][J] stores the minimum total distance for robot[0], ...robot[I] and factory[0], ... factory[J]
        mem = [[RESULT_MAX for _ in factory] for _ in robot]

        # if there is only factory[0]
        total = 0
        for I in range(factory[0][1]):
            # we have robot[0], ...robot[I]
            total += abs(robot[I] - factory[0][0])
            mem[I][0] = total

        # calculate mem[I][J] one-by-one
        # after analyzing the code, mem[I][J] actually only depends on mem[:I][J-1]
        for J in range(1, len(factory)):
            for I in range(len(robot)):
                # print(f"To calculate mem[{I}][{J}]: ")
                # print(robot[:I+1])
                # print(factory[:J+1])
                mem[I][J] = RESULT_MAX
                total = 0

                # i, j = current robot, current factory
                j = J
                flimit = factory[j][1]
                for i in range(I, -1, -1):
                    # if factory[j] has no rooms
                    if flimit == 0:
                        if j == 0: # there are robots left, but no more factories
                            # mem[I][J] = RESULT_MAX # we don't need this line (won't be set if cannot do recursion)
                            total = RESULT_MAX
                            break
                        j -= 1
                        flimit = factory[j][1]

                    # there is a "must-take" condition but we can skip it (not much difference)
                    if j > 0:
                        mem[I][J] = min(mem[I][J], total + mem[i][j-1])
                    
                    # robot[i] takes the factory[j]
                    total += abs(factory[j][0] - robot[i])
                    flimit -= 1
                    # print(f"robot[{i}] takes factory[{j}], total={total}")
                        
                mem[I][J] = min(mem[I][J], total)
                # print(f"mem[{I}][{J}] = {mem[I][J]}")
        return mem[-1][-1]
