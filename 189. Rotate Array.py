class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #len_nums = len(nums)
        for i in range(0,k,1):
            nums.insert(0,nums.pop())