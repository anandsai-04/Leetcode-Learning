class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        

            
        if len(nums)==2:
            if nums[0]==target:
                return 0
            elif nums[1]==target:
                return 1
            
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:#check if left is sorted
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1

                
            elif nums[mid]<=nums[right]:#check if right is sorted
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right=mid-1 
