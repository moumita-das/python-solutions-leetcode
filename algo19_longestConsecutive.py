class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        nums = sorted(list(set(nums)))
        max_sequence = 1
        counter = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                counter+=1
                max_sequence = counter if max_sequence < counter else max_sequence
            else:
                counter = 1
        return max_sequence


obj = Solution()
print(obj.longestConsecutive([1,2,0,1]))


# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 