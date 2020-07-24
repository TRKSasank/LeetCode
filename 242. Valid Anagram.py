class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        s_d = Counter(list(s))
        t_d = Counter(list(t))
        if(s_d == t_d):
            return True
        else:
            return False
        