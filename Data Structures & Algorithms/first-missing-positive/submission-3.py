class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)

    def firstMissingPositive(self, nums: List[int]) -> int:
        answer= 1
        
        for n in range(len(nums)):
            if answer in nums:
                answer += 1 
            else : 
                return answer
        return answer
    

    # Time complexity: O(nlon n)
    # Space complexity: O(n)
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     answer= 1
    #     sort_num = sorted(nums) # 선 정렬 진행
    #     for n in sort_num:
    #         if n > 0 and answer == n:
    #             answer += 1  
    #     return answer