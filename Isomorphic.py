class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        mps = {}
        mpt = set()
        
        for idx,c in enumerate(s):
            if c in mps:
                if mps[c] != t[idx]:
                    return False
            else:
                if t[idx] in mpt:
                    return False
                mpt.add(t[idx])
                mps[c] = t[idx]
                
        return True
