class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #from itertools import groupby
        import collections
        x_dict = Counter(nums)
        a = list(x_dict.values())
        a.sort(reverse=True)
        if(len(a) ==0 or a[0]==1):
            return False
        else:
            return True
        

        
