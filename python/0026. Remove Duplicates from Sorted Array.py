class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for the position of unique elements
        k = 1
        
        for i in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]  # Update the position with the new unique element
                k += 1  # Increment the count of unique elements
        
        return k
