class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count1 = {}
        for char in t:
            count1[char] = count1.get(char,0) + 1 
        count2 = {}
        need = len(count1)
        have = 0
        l = 0
        resL = float('infinity')
        indx = [-1,-1]
        for r in range(len(s)):
            count2[s[r]] = count2.get(s[r],0) + 1
            if s[r] in count1 and count1[s[r]] == count2[s[r]]:
                have+=1
            while need == have:
                if r-l+1 < resL:
                    resL = r-l+1
                    indx = [l,r]
                
                char_l = s[l]
                count2[char_l] -= 1
                if char_l in count1 and count2[char_l] < count1[char_l]:      
                    have-=1   
                l+=1
        l,r = indx
        return (s[l:r+1] if resL != float('infinity') else "")