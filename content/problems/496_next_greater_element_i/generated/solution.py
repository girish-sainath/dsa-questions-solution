from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find next greater element for each element in nums1 using nums2.
        
        Args:
            nums1: Query array (subset of nums2)
            nums2: Main array to find next greater elements in
            
        Returns:
            List of next greater elements for each element in nums1
        """
        # HashMap to store next greater element for each number in nums2
        next_greater = {}
        
        # Monotonic decreasing stack
        stack = []
        
        for num in nums2:
            # While stack has elements and current num is greater than top of stack
            # Current num is the "next greater element" for the top of stack
            while stack and num > stack[-1]:
                popped = stack.pop()
                next_greater[popped] = num
            
            stack.append(num)
        
        # Remaining elements in stack have no next greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Build result for nums1 using the hashmap
        return [next_greater[num] for num in nums1]


# ============= Test Cases =============
def test_solution():
    sol = Solution()
    
    # Test Case 1
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    result = sol.nextGreaterElement(nums1, nums2)
    print(f"Input: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result}")
    print(f"Expected: [-1, 3, -1]")
    print(f"Pass: {result == [-1, 3, -1]}\n")
    
    # Test Case 2
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    result = sol.nextGreaterElement(nums1, nums2)
    print(f"Input: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result}")
    print(f"Expected: [3, -1]")
    print(f"Pass: {result == [3, -1]}\n")
    
    # Test Case 3: Single element
    nums1 = [1]
    nums2 = [1]
    result = sol.nextGreaterElement(nums1, nums2)
    print(f"Input: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result}")
    print(f"Expected: [-1]")
    print(f"Pass: {result == [-1]}\n")
    
    # Test Case 4: All elements have next greater
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3, 4]
    result = sol.nextGreaterElement(nums1, nums2)
    print(f"Input: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result}")
    print(f"Expected: [2, 3, 4]")
    print(f"Pass: {result == [2, 3, 4]}\n")

test_solution()