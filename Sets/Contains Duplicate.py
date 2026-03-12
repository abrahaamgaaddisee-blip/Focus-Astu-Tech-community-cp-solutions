class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store=set()
        for a in nums:
            store.add(a)
        if len(nums)==len(store):
            return alse
        else:
            return True
