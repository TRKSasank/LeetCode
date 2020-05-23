class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        i =0
        while i < len(s):
            
            if(s[i] == 'M'):
                count = count + 1000
                i=i+1
                continue
                
            if(s[i] == 'D'):
                count = count + 500
                i=i+1
                continue
                
            if(s[i] == 'C'):
                if(i+1 < len(s) and s[i+1] == 'D'): 
                    count = count + 400
                    i=i+2
                    if(i == len(s)):
                        break
                    else:
                        continue
                elif(i+1 < len(s) and s[i+1] == 'M'):
                    count = count + 900
                    i=i+2
                    if(i == len(s)):
                        break
                    else:
                        continue
                else:
                    count = count + 100
                    i=i+1
                    continue
            
        
            if(s[i] == 'L'):
                count = count + 50
                i=i+1
                continue
                
                
            if(s[i] == 'X'):
                if(i+1 < len(s) and s[i+1] == 'L'): 
                    count = count + 40
                    i=i+2
                    if(i == len(s)):
                        break
                    else:
                        continue
                elif(i+1 < len(s) and s[i+1] == 'C'):
                    count = count + 90
                    i=i+2
                    if(i == len(s)):
                        break
                    else:
                        continue
                else:
                    count = count + 10
                    i=i+1
                    continue            
            
            if(s[i] == 'V'):
                count = count + 5
                i=i+1
                continue

            if(s[i] == 'I'):
                if(i+1 < len(s) and s[i+1] == 'V'):
                    count = count + 4
                    i=i+2
                    if(i == len(s)):
                        break
                    else:
                        continue
                elif(i+1 < len(s) and s[i+1] == 'X'):
                    count = count + 9
                    i=i+2
                    if(i == len(s)):
                        break
                    else:
                        continue
                else:
                    count = count + 1
                    i=i+1
                    continue

        return(count)
        