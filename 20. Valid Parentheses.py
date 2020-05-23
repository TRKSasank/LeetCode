class Solution:
    def isValid(self, s: str) -> bool:
        ls = list(s)
        k =0
        dict_t = {"(":")","[":"]","{":"}",")":"(","]":"[","}":"{"}
        while k+1 < len(ls) :
            if(dict_t[ls[k]] == ls[k+1]):
                ls.pop(k) 
                ls.pop(k)
                k=0
                continue
            k=k+1
        if(len(ls) == 0):
            return(True)
        else: 
            return(False)           
        