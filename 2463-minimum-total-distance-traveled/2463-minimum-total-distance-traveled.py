class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # from outside to inside
        # can move robot or factory (but factory doesn't have to fulfil)
        # if a robot has chosen one direction, it can just take the nearest factory (no need to go further unless the factory is already full), including the one it already locates
        # thus, outer robots have no choices
        robot.sort()

        # clear empty factories and sort
        newFactory = []
        for fpos, flimit in factory:
            if flimit > 0:
                newFactory.append((fpos, flimit))
        factory = newFactory
        factory.sort()
        
        # print(robot)
        # print(factory)
        
        @cache
        def dp(x, y):
            """
            Give the result starting from robot[x] and factory[y],
            ignoring the previous items
            
            x < R
            factory[y] must be new (not filled by any robot)
            """
            # print(f"dp({x}, {y})")
            result = 2**63-1

            total = 0
            if y >= len(factory):
                return 2**63-1

            fpos, flimit = factory[y]
            for i in range(x, len(robot)):

                rpos = robot[i]

                # if empty factory, step next
                while True:
                    if flimit > 0:
                        break
                    # print(f"factory[{y}] is full")
                    y += 1
                    if y >= len(factory):
                        return 2**63-1
                    fpos, flimit = factory[y]

                # conditions that robot[i] must take factory[y]
                # debug = f"(DEBUG: {rpos}, {(fpos, flimit)}"
                # if y + 1 < len(factory):
                    # debug += f", {factory[y + 1]})"
                    
                mustTake = False
                if rpos <= fpos:
                    # outer robot
                    mustTake = True
                elif y + 1 < len(factory):
                    # inner, but closer to the factory[y]
                    fpos1, flimit1 = factory[y + 1]
                    if abs(fpos - rpos) <= abs(fpos1 - rpos):
                        mustTake = True
                
                if not mustTake:
                    # may try the alternative that it doesn't take the factory
                    # then, that factory must be removed (impossible to get better)
                    # print(f"robot[{i}] tries not to take factory[{y}] {debug}")
                    alternative = total + dp(i, y + 1)
                    # print(f"robot[{i}] tries not to take factory[{y}] done {debug}")
                    result = min(result, alternative)
                
                # take it anyway
                # print(f"robot[{i}] takes factory[{y}] {debug}")
                total += abs(fpos - rpos)
                flimit -= 1
            result = min(result, total)
            return result
        
        return dp(0, 0)