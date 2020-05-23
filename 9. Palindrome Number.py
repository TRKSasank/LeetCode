class Solution:
    def isPalindrome(self, x: int) -> bool:
        Retrun_val = False 
        x_check = x
        if(x == 0):
            Retrun_val = True 
        elif(x < 0):
            Retrun_val = False       
        elif(x > 0):
            final = 0
            len_digit = len(str(x))
            for i in range(0,len_digit):
                Temp = 0
                Temp =  (x % 10)
                x = int(x/10)
                if Temp != 0:
                    final = final + Temp * pow(10,len_digit-i-1)     
            if (final == x_check):
                Retrun_val = True 
        return(Retrun_val)
        