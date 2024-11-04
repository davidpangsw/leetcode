class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        ch, count = word[0], 1
        word += "_"
        for c in word[1:]:
            if c == ch:
                count += 1
            else:
                q, r = count // 9, count % 9
                comp += (f"9{ch}" * q)
                if r > 0:
                    comp += f"{r}{ch}"
                ch = c
                count = 1
        return comp