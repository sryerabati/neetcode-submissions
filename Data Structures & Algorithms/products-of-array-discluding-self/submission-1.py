class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        res = []

        for num in nums:
            if num != 0 :
                product = product * num
            else:
                zeroCount += 1

        for n in nums:
            if zeroCount >= 2:
                res.append(0)
            elif zeroCount == 1:
                if n == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(product // n)
        
        return res