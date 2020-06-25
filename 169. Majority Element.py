class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unqnums = list(set(nums))
        count = 0

        for i in unqnums:
            if(count < nums.count(i) ):
                count = nums.count(i)
                val = i
                
        return val
        