class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        answer= 1
        
        for n in range(len(nums)):
            if answer in nums:
                answer += 1 
            else : 
                return answer
        return answer