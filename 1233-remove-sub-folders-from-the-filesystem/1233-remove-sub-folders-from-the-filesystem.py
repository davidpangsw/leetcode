class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
        for i in range(1, len(folder)):
            f = folder[i]
            # print(result, f)
            ind = f.rfind('/')
            if f[:ind+1].startswith(result[-1]):
                continue
            result.append(f)


        return result
        