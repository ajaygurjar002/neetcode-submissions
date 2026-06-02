class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        result = []
        for i in range(len(nums)):
            index[nums[i]] = i
        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in index and j!=index[diff]:
                return [j,index[diff]]
        
        
        