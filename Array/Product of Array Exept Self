class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[1]*n
        prifix=1
        for i in range(n):
            arr[i]=prifix
            prifix*=nums[i]
        postfix=1
        for i in range(n-1,-1,-1):
             arr[i]*=postfix
             postfix*=nums[i]
        return arr
