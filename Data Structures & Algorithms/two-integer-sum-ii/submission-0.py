class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i<len(numbers):
            t = target - numbers[i]
            if t in numbers[i+1:]:
                return [i+1,numbers.index(t)+1]
            i+=1
        