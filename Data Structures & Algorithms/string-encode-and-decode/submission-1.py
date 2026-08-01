class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], []
        for s in strs:
            sizes.append(len(s))
        for i in range(0, len(sizes), 1):

            res.append(str(sizes[i]))
            res.append('#')
            res.append(strs[i])
        print(''.join(res))
        return ''.join(res)
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        sizeBuilder = ""
        size = 0

        while i < len(s):
            if s[i] == "#":
                size = int(sizeBuilder)
                res.append(s[i+1:i+1+size])
                i = i+size+1
                sizeBuilder = ""
            else:
                sizeBuilder = sizeBuilder + s[i]
                i += 1
        return res