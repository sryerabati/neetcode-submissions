from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        result = deque()

        map = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for c in s:
            if c in list(map.values()):   
                result.append(c);
            elif result and result[-1] == map.get(c):
                result.pop();
            else:
                return False;
        
        if len(result) == 0:
            return True;
        return False;


