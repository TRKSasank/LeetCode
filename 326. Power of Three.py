class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if(n<0):
            val = math.log(n*-1,3)
            val_c = math.ceil(val)
            val_f = math.floor(val)
        elif(n>0):
            val = math.log(n,3)
            val_c = math.ceil(val)
            val_f = math.floor(val)
        else:
            return False
        if(n>=1 and (n == 3**val_c or n == 3**val_f) ):
            return True
        #elif(n<0 and (n == (-3)**val_c or n == (-3)**val_f) ):
        #    return True
        else:
            return False
        
        
        