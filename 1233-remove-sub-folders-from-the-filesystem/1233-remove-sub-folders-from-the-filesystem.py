def insert(tree, path, start):
    # print(tree, path, start)
    if "data" in tree:
        return False # early stop, not mandatory
    
    if start == len(path):
        tree["data"] = path
        return True

    ind = path.find('/', start + 1)
    if ind == -1:
        ind = len(path)
    key = path[start:ind]
    if key not in tree:
        tree[key] = {}
    
    return insert(tree[key], path, ind)

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
            insert(tree, f, 0)
        # print("Printing")
        return [x for x in collect(tree)]
        