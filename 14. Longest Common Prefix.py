class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match_str = ""
        check = 0
        count = 0
        
        if(len(strs) == 0):
            return(match_str)
        elif(len(strs) == 1 ):
            match_str = strs[0]
            return(match_str)
        
        strs_short = strs[min((len(x),strs.index(x)) for x in strs )[1]]    
        strs_short_len = len(strs_short)
        strs.remove(strs_short)
        for j in range(len(strs_short),0,-1):
            for i in range(0,len(strs)):   
                if((strs[i][0:j] == strs_short[0:j])):
                    match_str = strs[i][0:j]
                    count = count + 1 
                    continue
            if(count == len(strs)):
                print(match_str)
                return(match_str)
                break
            else:
                count = 0
                match_str = ""
        return(match_str)