from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find minimum element in rotated sorted array using binary search.
        
        Args:
            nums: Rotated sorted array of unique elements
            
        Returns:
            The minimum element in the array
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than right element,
            # minimum must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, minimum is in the left half (including mid)
            else:
                right = mid
        
        # left == right, pointing to the minimum element
        return nums[left]


# Test cases
def test_solution():
    solution = Solution()
    
    # Test Case 1: Rotated array
    nums1 = [3, 4, 5, 1, 2]
    result1 = solution.findMin(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: 1")
    print(f"Pass: {result1 == 1}\n")
    
    # Test Case 2: Rotated array with zero
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    result2 = solution.findMin(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: 0")
    print(f"Pass: {result2 == 0}\n")
    
    # Test Case 3: No rotation (sorted array)
    nums3 = [11, 13, 15, 17]
    result3 = solution.findMin(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: 11")
    print(f"Pass: {result3 == 11}\n")
    
    # Test Case 4: Single element
    nums4 = [1]
    result4 = solution.findMin(nums4)
    print(f"Input: {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: 1")
    print(f"Pass: {result4 == 1}\n")
    
    # Test Case 5: Two elements
    nums5 = [2, 1]
    result5 = solution.findMin(nums5)
    print(f"Input: {nums5}")
    print(f"Output: {result5}")
    print(f"Expected: 1")
    print(f"Pass: {result5 == 1}\n")


if __name__ == "__main__":
    test_solution()