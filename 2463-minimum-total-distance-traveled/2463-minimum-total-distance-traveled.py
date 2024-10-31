INT_MAX = 2 * 10**9 * 100
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # figure out some basic rules first
        # factories with limit=0 are meaningless
        # if a robot has chosen one direction, it can just take the nearest factory (no need to go further unless the factory is already full), including the one it already locates
        # outer robots have no choices

        # sort the robots
        robot.sort()

        # clear factories and sort
        factory = [(fpos, flimit) for fpos, flimit in factory if flimit > 0]
        factory.sort()
        
        print(robot)
        print(factory)

        @cache
        def dp(x, y):
            """
            Give the result starting from robot[x] and factory[y],
            where factory[y] is empty
            ignoring the previous items
            
            x < R
            factory[y] must be new (not filled by any robot)
            """
            result = INT_MAX

            total = 0
            if y >= len(factory):
                return INT_MAX

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
                    print(i, y)
                    y += 1
                    if y < len(factory):
                        fpos, flimit = factory[y]
                    elif i + 1 < len(robot):
                        return INT_MAX
            result = min(result, total)
            return result
        
        return dp(0, 0)