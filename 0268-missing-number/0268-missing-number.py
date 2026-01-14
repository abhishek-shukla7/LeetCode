class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dict={}

        for i in range(0,n+1):
            dict[i]=0

        for nu in nums:
            dict[nu]=1

        for k,u in dict.items():
            if u==0:
                return k
        