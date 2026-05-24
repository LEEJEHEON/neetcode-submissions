class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target == nums[len(nums)//2] : 
            return len(nums)//2
        
        
        elif (target > nums[len(nums)//2] ):
            for n in range(len(nums)//2, len(nums)) :
                if target == nums[n]:
                    return n
        else :
            for n in range(0, len(nums)//2):
                if target == nums[n]:
                    return n 
        return -1 
         