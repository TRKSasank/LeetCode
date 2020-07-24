class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = [] 
        for i in nums1:
            if(nums2.count(i) >=1):
                final.append(i)
                nums2.remove(i)
                
        return final
                
                
            
        
        
        