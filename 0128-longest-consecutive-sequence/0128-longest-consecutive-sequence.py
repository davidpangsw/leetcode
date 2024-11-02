class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # result = 0
        # groups = []
        # elemToGroup = {}
        # for x in nums:
        #     print("Adding ", x)
        #     if x in elemToGroup:
        #         continue
        #     elif x+1 in elemToGroup and x-1 in elemToGroup:
        #         result = max(result, elemToGroup[x-1] + 1 + elemToGroup[x+1])
        #     elif x+1 in elemToGroup:
        #     elif x-1 in elemToGroup:
        #     else:
        # return result

        result = 0
        groups = []
        elemToGroup = {}
        for x in nums:
            # print("Adding ", x)
            if x in elemToGroup:
                continue
            elif x+1 in elemToGroup and x-1 in elemToGroup:
                # merge
                # print("Merge...")
                g1 = elemToGroup[groups[elemToGroup[x-1]][0]]
                g2 = elemToGroup[groups[elemToGroup[x+1]][1]]
                # print(x-1, x+1, groups[g1], groups[elemToGroup[g2]])

                groups[g1][1] = groups[g2][1]
                # groups[g2][0] = groups[g1][0]

                groups[g2] = groups[g1] # key: change by reference!
                
                g = g1
                # print(groups[elemToGroup[x-1]], groups[elemToGroup[x+1]])
            elif x+1 in elemToGroup:
                g = elemToGroup[x+1]
                groups[g][0] = x
            elif x-1 in elemToGroup:
                g = elemToGroup[x-1]
                groups[g][1] = x
            else:
                g = len(groups)
                groups.append([x, x])
            elemToGroup[x] = g
            result = max(result, groups[g][1] + 1 - groups[g][0])

            # print(groups, elemToGroup)
        return result
