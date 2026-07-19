from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert to set for O(1) lookups and remove duplicates
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting if this is the beginning of a sequence
            # (i.e., num - 1 is NOT in the set)
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Extend the sequence as far as possible
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update the maximum length
                max_length = max(max_length, current_length)
        
        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = solution.longestConsecutive(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")  # Expected: 4
    print()
    
    # Example 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result2 = solution.longestConsecutive(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")  # Expected: 9
    print()
    
    # Example 3
    nums3 = [1, 0, 1, 2]
    result3 = solution.longestConsecutive(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")  # Expected: 3
    print()
    
    # Edge case: empty array
    nums4 = []
    result4 = solution.longestConsecutive(nums4)
    print(f"Input: {nums4}")
    print(f"Output: {result4}")  # Expected: 0