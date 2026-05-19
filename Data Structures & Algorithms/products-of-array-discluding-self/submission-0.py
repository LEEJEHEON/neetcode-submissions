class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for n in range(len(nums)) :
            l = nums.copy() # copy를 안하면 pop 할때 nums 도 같이 날라감 
            l.pop(n)
            answer.append(l[0])
            for m in range(1, len(l)):
                answer[n] *= l[m]
        return answer
