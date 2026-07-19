from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Number of rows and columns
        num_rows = len(strs)
        num_cols = len(strs[0])
        
        # Counter for columns to delete
        delete_count = 0
        
        # Iterate through each column
        for col in range(num_cols):
            # Check if column is sorted (non-decreasing order)
            for row in range(1, num_rows):
                # If current character is less than previous character
                # the column is not sorted
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break  # No need to check further for this column
        
        return delete_count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    strs1 = ["cba", "daf", "ghi"]
    result1 = solution.minDeletionSize(strs1)
    print(f"Input: strs = {strs1}")
    print(f"Output: {result1}")  # Expected: 1
    print()
    
    # Example 2
    strs2 = ["a", "b"]
    result2 = solution.minDeletionSize(strs2)
    print(f"Input: strs = {strs2}")
    print(f"Output: {result2}")  # Expected: 0
    print()
    
    # Example 3
    strs3 = ["zyx", "wvu", "tsr"]
    result3 = solution.minDeletionSize(strs3)
    print(f"Input: strs = {strs3}")
    print(f"Output: {result3}")  # Expected: 3

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Using zip to iterate through columns and all() for checking order
        return sum(
            1 for col in zip(*strs)  # Transpose: each 'col' is a tuple of chars
            if col != tuple(sorted(col))  # Check if column is not sorted
        )