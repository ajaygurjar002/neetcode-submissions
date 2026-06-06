class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,num in enumerate(nums):
            if num>0:
                break
            if i>0 and num == nums[i-1]:
                continue
            
            k=i+1
            j=len(nums)-1
            while k<j:
                if num+nums[k]+nums[j]<0:
                    k+=1
                    
                elif num+nums[k]+nums[j]>0:
                    j-=1
                    
                else:
                    tmp = [num,nums[k],nums[j]]
                    res.append(tmp)
                    k+=1
                    j-=1
                    while nums[k] == nums[k - 1] and k < j:
                        k += 1
                    
        return res
            
                    
        

        