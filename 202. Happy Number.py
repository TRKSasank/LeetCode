class Solution:
    def isHappy(self, n: int) -> bool:
        counter = 0
        flag = False
        list_val = []
        while(flag != True):
            rem = n %10
            n = int(n/10)
            counter = counter + rem*rem
            if(n ==0 and counter == 1 ):
                return True
            if(n ==0 ):
                n=counter
                if(list_val.count(counter) >=1 ):
                    return False
                list_val.append(counter)
                counter = 0
        
            
        
        
        
    