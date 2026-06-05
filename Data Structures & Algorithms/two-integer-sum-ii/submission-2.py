class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,num in enumerate(numbers):
            t = target - num
            l = i+1
            j= len(numbers)-1
            
            while l<=j:
                mid = (l+j)//2
                if t>numbers[mid]:
                    l=mid+1
                elif t<numbers[mid]:
                    j=mid-1
                else:
                    return [i+1,mid+1]
                



        
        