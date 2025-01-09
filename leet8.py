class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        original_nums = nums
        nums = []
        ## cleanup to remove continuos duplicates
        for i in range(len(original_nums)):
            if i==0:
                nums.append(original_nums[i])
                continue
            if original_nums[i]==nums[len(nums)-1]:
                continue
            nums.append(original_nums[i])

        for i in range(len(nums)-1):
            if i==0:
                continue
            left_min = min(nums[0:i])
            right_max = max(nums[i+1: len(nums)])
            if left_min<nums[i]<right_max:
                return True
        return False

obj = Solution()
print(obj.increasingTriplet([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))