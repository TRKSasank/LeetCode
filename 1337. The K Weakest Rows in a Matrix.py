class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        import numpy as np
        y = dict(enumerate(list(np.array(mat).sum(axis=1))))
        return list({k: v for k, v in sorted(y.items(), key=lambda item: item[1])}.keys())[0:k]