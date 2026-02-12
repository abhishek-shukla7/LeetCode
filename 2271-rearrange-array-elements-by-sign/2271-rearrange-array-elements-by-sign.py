class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n=len(nums)
        pos=[]
        neg=[]
        for i in range(0,n):
            if nums[i]>0:
                pos.append(nums[i])
        for i in range(0,n):
            if nums[i]<0:
                neg.append(nums[i])


        for i in range (0,len(pos)):
            nums[2*i]=pos[i]
            nums[(2*i)+1]=neg[i]
        
        return nums
            
        