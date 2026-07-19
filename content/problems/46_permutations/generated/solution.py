from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(current_perm, remaining):
            # Base case: if no remaining numbers, we have a complete permutation
            if not remaining:
                result.append(current_perm[:])  # Add a copy of current permutation
                return
            
            # Try each remaining number as the next element
            for i in range(len(remaining)):
                # Choose: add nums[i] to current permutation
                current_perm.append(remaining[i])
                
                # Explore: recurse with remaining numbers (excluding nums[i])
                backtrack(current_perm, remaining[:i] + remaining[i+1:])
                
                # Un-choose (backtrack): remove the last added element
                current_perm.pop()
        
        backtrack([], nums)
        return result


# ============================================================
# Test Cases
# ============================================================
def run_tests():
    solution = Solution()
    
    # Test Case 1
    nums = [1, 2, 3]
    output = solution.permute(nums)
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(f"Input: {nums}")
    print(f"Output: {output}")
    print(f"Expected: {expected}")
    print(f"Match: {sorted(output) == sorted(expected)}\n")
    
    # Test Case 2
    nums = [0, 1]
    output = solution.permute(nums)
    expected = [[0,1],[1,0]]
    print(f"Input: {nums}")
    print(f"Output: {output}")
    print(f"Expected: {expected}")
    print(f"Match: {sorted(output) == sorted(expected)}\n")
    
    # Test Case 3
    nums = [1]
    output = solution.permute(nums)
    expected = [[1]]
    print(f"Input: {nums}")
    print(f"Output: {output}")
    print(f"Expected: {expected}")
    print(f"Match: {sorted(output) == sorted(expected)}\n")

run_tests()