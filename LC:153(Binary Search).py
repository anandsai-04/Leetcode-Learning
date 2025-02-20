#how binary search works
# define left as 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 #define left at index 0 and right in other end
        right = len(nums)-1
        while left < right: # if middle term is less than right term all elements before middle term are cut, so middle term is the new left term
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1#else if middle is more than right all terms after middle are cut, making middle term the new right term
            else:
                right=mid#the process goes on until left<right condition is not satified
        return nums[left]
