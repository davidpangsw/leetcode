def collect(tree):
    # print(tree)
    if "data" in tree:
        yield tree["data"]
        return

    for key in tree:
        for x in collect(tree[key]):
            yield x

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        tree = {}
        for f in folder:
            start = 0
            cur = tree
            while start < len(f):
                end = f.find('/', start+1)
                if end == -1:
                    end = len(f)
                key = f[start:end]
                if "data" in cur:
                    break
                if key not in cur:
                    cur[key] = {}
                cur = cur[key]

                start = end
            if "data" not in cur:
                cur["data"] = f

        # print("Printing")
        return [x for x in collect(tree)]
        