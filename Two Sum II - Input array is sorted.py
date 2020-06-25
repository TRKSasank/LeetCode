class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while(i<j):
            x = numbers[i]+numbers[j]
            if(x<target):
                i=i+1
            elif(x>target):
                j=j-1
            else:
                return([i+1,j+1])

            
        return[0,0]
        
        
    
