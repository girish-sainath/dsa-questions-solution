from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current_subset: List[int]):
            # Add the current subset to result (including empty set)
            result.append(current_subset[:])
            
            # Try adding each remaining element to the current subset
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                current_subset.append(nums[i])
                
                # Recurse with the next index
                backtrack(i + 1, current_subset)
                
                # Backtrack: remove the last element to try other combinations
                current_subset.pop()
        
        backtrack(0, [])
        return result


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 2, 3]
    result1 = solution.subsets(nums1)
    print(f"Input: nums = {nums1}")
    print(f"Output: {result1}")
    print(f"Total subsets: {len(result1)}")  # Should be 2^3 = 8
    
    print()
    
    # Test Case 2
    nums2 = [0]
    result2 = solution.subsets(nums2)
    print(f"Input: nums = {nums2}")
    print(f"Output: {result2}")
    print(f"Total subsets: {len(result2)}")  # Should be 2^1 = 2