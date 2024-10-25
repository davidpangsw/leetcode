class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = set()
        for f in sorted(folder):
            # print(result, f)
            start = 0
            while start < len(f):
                # print("    " + str(tree))

                end = f.find('/', start+1)
                if end == -1:
                    end = len(f)
                    result.add(f[:end])
                    break

                key = f[:end]
                if key in result:
                    break
                

                start = end

        return list(result)
        