class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums.sort()
        count=0
        smaller_longest=float("-inf")
        longest=0

        for i in range(0,n):
            num=nums[i]
            if num-1==smaller_longest:
                count+=1
                smaller_longest=num
            elif num!=smaller_longest:
                count=1
                smaller_longest=num

            longest=max(longest,count)
        return longest