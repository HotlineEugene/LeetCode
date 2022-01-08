class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
	    n = len(nums)
	    dic = {} 
	    for i in range(0,n):
		    if dic.get(target-nums[i])!=None:
			    return [i,dic[target-nums[i]]];
		    dic[nums[i]]=i
	    return []
        
