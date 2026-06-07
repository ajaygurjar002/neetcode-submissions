class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count2 = {}
        for char in s1:
            count2[char] = count2.get(char,0) + 1
        need = len(count2)       
        for l in range(len(s2)): 
            count1, curr= {},0       
            for r in range(l,len(s2)):            
                count1[s2[r]] = count1.get(s2[r],0) + 1
                if count2.get(s2[r],0)<count1.get(s2[r],0):
                    break
                if count2.get(s2[r],0)==count1.get(s2[r],0):
                    curr+=1
                if curr == need:
                    return True           
        return False


        