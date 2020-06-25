class Solution:
    def convertToTitle(self, n: int) -> str:
        str_final = [ 'a' ]
        import math
        dict_alpha ={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',0:'z',26:'z'}
        prev_cycle_val = 0
        
        def index_val_fn(str_final):
            for k in range(0,len(str_final),1):
                if(str_final[k] != 'z'):
                    index_val = str_final[k]
                    return index_val,k
                
        for i in range(1,n+1,1):
            ##append for each cycle     
            if(i>26 and i%26 ==1 and str_final.count('z')==len(str_final) and math.log(i-prev_cycle_val -1,26).is_integer() ):
                str_final = ['a'] * (int(math.log(i-prev_cycle_val -1,26)) + 1)
                prev_cycle_val = i -1
            ##update on position 
            elif(i%26 >= 2 or i%26 == 0 ):
                str_final[0] = dict_alpha[i%26]
            elif( i%26 == 1):
                if(len(str_final) == 1 ):
                    str_final[0] = dict_alpha[1]
                if(len(str_final) > 1):
                    index_val,k = index_val_fn(str_final)
                    key = list(dict_alpha.keys())[list(dict_alpha.values()).index(index_val)]   
                    str_final[k] = dict_alpha[(key+1)]
                    for l in range(0,k,1):
                        str_final[l] = 'a'
         
        
        
        str_final.reverse()
        final = ''
        for m in str_final:
            final = final + m
        
        return final.upper()
