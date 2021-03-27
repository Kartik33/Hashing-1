from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            temp = [0]*26
            for c in s:
                temp[ord(c)-ord('a')] += 1
                
            temp = tuple(temp)
            groups[temp].append(s)
            
        return list(groups.values())
