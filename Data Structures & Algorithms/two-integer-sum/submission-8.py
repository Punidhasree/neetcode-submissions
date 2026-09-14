class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums=[(num,i) for i, num in enumerate(nums)]
        nums.sort()
        j=len(nums)-1
        i=0
        while i<j:
            total=nums[i][0]+nums[j][0]
            if total==target:
                return sorted([nums[i][1],nums[j][1]])
            elif total>target:
                j-=1
            else:
                i+=1


        