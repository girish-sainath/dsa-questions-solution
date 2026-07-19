from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target and return their indices.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing the two indices
        """
        # Hash map to store {number: index}
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our hash map
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        return []  # No solution found (per constraints, this won't happen)


# ---- Test Cases ----
def run_tests():
    solution = Solution()
    
    # Test Case 1
    nums1, target1 = [2, 7, 11, 15], 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Output: {result1}")
    print(f"Expected: [0, 1] -> {'PASS' if result1 == [0, 1] else 'FAIL'}\n")
    
    # Test Case 2
    nums2, target2 = [3, 2, 4], 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Test 2: nums={nums2}, target={target2}")
    print(f"Output: {result2}")
    print(f"Expected: [1, 2] -> {'PASS' if result2 == [1, 2] else 'FAIL'}\n")
    
    # Test Case 3
    nums3, target3 = [3, 3], 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3}")
    print(f"Output: {result3}")
    print(f"Expected: [0, 1] -> {'PASS' if result3 == [0, 1] else 'FAIL'}\n")

run_tests()