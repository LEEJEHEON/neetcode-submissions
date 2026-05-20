class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        answer= 1
        sort_num = sorted(nums) # 선 정렬 진행
        for n in sort_num:
            if n > 0 and answer == n:
                answer += 1  
        return answer