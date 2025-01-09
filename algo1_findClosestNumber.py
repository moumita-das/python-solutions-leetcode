class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        smallest = nums[0]
        for i in range(1,len(nums)):
            if(abs(nums[i])<abs(smallest)):
                smallest=nums[i]
            elif(abs(nums[i])==abs(smallest) and nums[i]>smallest):
                smallest=nums[i]

