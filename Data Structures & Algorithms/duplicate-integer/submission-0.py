class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp={}
        cnt=0
        for i in nums:
            if i in mapp:
                mapp[i]+=1
                cnt+=1
            else:
                mapp[i]=i
        if cnt>0:
            return True
        return False

                