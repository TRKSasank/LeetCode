
class Solution:
    def reverse(self, x: int) -> int:
        
        if(x == 0):
            final = 0
        elif(x < 0):
            x = x * -1     
            final = 0
            len_digit = len(str(x))
            for i in range(0,len_digit) :
                Temp = 0
                Temp =  (x % 10)
                x = int(x/10)
                if Temp != 0:
                    final = final + Temp * pow(10,len_digit-i-1)
#                    print(Temp , '====', 'power', len_digit-i-1, "final" ,final)     
            final = final * -1
            if (final < -2147483648 or  final > 2147483647):
                final = 0
    
        elif(x > 0):
            final = 0
            len_digit = len(str(x))
            for i in range(0,len_digit) :
                Temp = 0
                Temp =  (x % 10)
                x = int(x/10)
                if Temp != 0:
                    final = final + Temp * pow(10,len_digit-i-1)
#            print(Temp , '====', 'power', len_digit-i-1, "final" ,final)
            if (final < -2147483648 or  final > 2147483647):
                final = 0

        return(final)