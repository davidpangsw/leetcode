RESULT_MAX = 2 * (10**9) * 100
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # sort the robots
        robot.sort()

        # clear factories and sort
        factory = [(fpos, flimit) for fpos, flimit in factory if flimit > 0]
        factory.sort()

        # print(robot)
        # print(factory)

        # mem[I][J] stores the minimum total distance for robot[0], ...robot[I] and factory[0], ... factory[J]
        # mem[I][J] only depends on mem[:I][J-1]
        mem = [[RESULT_MAX for _ in factory] for _ in robot]

        for J in range(len(factory)):
            for I in range(len(robot)):
                # print(f"To calculate mem[{I}][{J}]: ")
                # print(robot[:I+1])
                # print(factory[:J+1])
                # To calculate mem[I][J]
                # suppose we have only robot[0], ...robot[I] and factory[0], ... factory[J]
                result = RESULT_MAX
                total = 0

                # i, j = current robot, current factory
                j = J
                fpos, flimit = factory[j]
                for i in range(I, -1, -1):
                    rpos = robot[i]

                    # conditions that robot[i] must take factory[j] :
                    # outer robot; or
                    # inner robot but closer to the factory[j]
                    # if j > 0:
                    #     print(f"{rpos} {factory[j-1]} {factory[j]}")
                    # else:
                    #     print(f"{rpos} {factory[j]}")
                    mustTake = (rpos >= fpos) or (j - 1 >= 0 and abs(fpos - rpos) <= abs(factory[j-1][0] - rpos))
                    if not mustTake:
                        # may try the optional alternative that it doesn't take the factory
                        # in this case, that factory must be removed (impossible to get better result if we keep it)
                        result = min(result, total + mem[i][j-1] if j > 0 else RESULT_MAX)
                        # print(f"robot[{i}] try not to take factory[{j}], {total + mem[i][j-1] if j > 0 else RESULT_MAX}")

                    # take the factory
                    total += abs(fpos - rpos)
                    flimit -= 1
                    # print(f"robot[{i}] takes factory[{j}], total={total}")

                    # if factory has no rooms
                    if flimit == 0:
                        j -= 1
                        if j >= 0:
                            fpos, flimit = factory[j]
                        elif i > 0: # there are robots left, but no more factories
                            # print("No more factories!")
                            result = RESULT_MAX
                            total = RESULT_MAX
                            break
                mem[I][J] = min(result, total)
                # print(f"mem[{I}][{J}] = {mem[I][J]}")
        return mem[-1][-1]



    def minimumTotalDistanceOld(self, robot: List[int], factory: List[List[int]]) -> int:
        # figure out some basic rules first
        # factories with limit=0 are meaningless
        # if a robot has chosen one direction, it can just take the nearest factory (no need to go further unless the factory is already full), including the one it already locates
        # outer robots have no choices

        # sort the robots
        robot.sort()

        # clear factories and sort
        factory = [(fpos, flimit) for fpos, flimit in factory if flimit > 0]
        factory.sort()
        
        # print(robot)
        # print(factory)

        @cache
        def dp(x, y):
            """
            Return the result starting from robot[x] and factory[y],
            where factory[y] is empty
            ignoring the previous items
            
            x < R
            factory[y] must be new (not filled by any robot)
            """
            result = RESULT_MAX

            total = 0
            if y >= len(factory):
                return RESULT_MAX

            fpos, flimit = factory[y]
            for i in range(x, len(robot)):
                rpos = robot[i]

                # conditions that robot[i] must take factory[y] :
                # outer robot; or
                # inner robot but closer to the factory[y]
                mustTake = (rpos <= fpos) or (y + 1 < len(factory) and abs(fpos - rpos) <= abs(factory[y + 1][0] - rpos))
                if not mustTake:
                    # may try the optional alternative that it doesn't take the factory
                    # in this case, that factory must be removed (impossible to get better result if we keep it)
                    result = min(result, total + dp(i, y + 1))
                
                # take the factory
                total += abs(fpos - rpos)
                flimit -= 1

                # if factory is full, use next one
                if flimit == 0:
                    y += 1
                    if y < len(factory):
                        fpos, flimit = factory[y]
                    elif i + 1 < len(robot):
                        return RESULT_MAX
            return min(result, total)
        
        return dp(0, 0)