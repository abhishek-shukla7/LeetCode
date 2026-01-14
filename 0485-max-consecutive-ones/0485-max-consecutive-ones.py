class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        count=0
        max_count=0
        while i<n:
            if nums[i]==1:
                count+=1
                max_count=max(max_count,count)
            else:
                count=0
            i+=1
        return max_count
        