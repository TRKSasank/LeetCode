import math 
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for i in list(range(1,len(str(n))+100,1)):
            count = count + int(n/(5 ** i)) 
        return count
                