class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = []
        tree = {}
        for f in sorted(folder):
            # print(tree, f)
            start = 0
            cur = tree
            while start < len(f):
                # print("    " + str(tree))
                if "data" in cur:
                    break

                end = f.find('/', start+1)
                if end == -1:
                    end = len(f)


                key = f[start:end]
                if key not in cur:
                    cur[key] = {}
                cur = cur[key]

                start = end

            if "data" not in cur:
                cur["data"] = f
                result.append(f)

        return result
        