class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0
        l = 0 
        r= l+1
        ns = set()
        ns.add(s[l])
        maxL = 1
        while r<len(s): 
            if s[r] not in ns:
                ns.add(s[r])
                maxL=max(maxL,len(ns))
                r+=1
            else:
                ns.remove(s[l])
                l+=1 
        return maxL


        