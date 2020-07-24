class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = 0
        count = 0
        counter = nums.count(0)
        while(i<len_nums):
            if(counter == count ):
                break
            if(nums[i] == 0):
                nums.pop(i)
                nums.insert(len_nums,0)
                count = count +1
                i= i-1
            i = i +1