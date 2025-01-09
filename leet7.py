class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1]
        while(n>=2):
            result.append(nums[n-1] * result[len(result)-1])
            n-=1
        result = result[::-1]
        prev_multiple = nums[0]
        for i in range(len(nums)):
            if(i==0):
                continue
            elif i==len(nums)-1:
                result[i]=prev_multiple
                return result
            result[i] = result[i] * prev_multiple
            prev_multiple = prev_multiple * nums[i]




obj = Solution()
print(obj.productExceptSelf([-1,1,0,-3,3]))