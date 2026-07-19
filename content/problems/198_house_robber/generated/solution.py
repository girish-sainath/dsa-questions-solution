from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]
        
        # Edge case: only two houses
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Initialize dp array
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill dp table
        for i in range(2, len(nums)):
            # Either skip current house (dp[i-1])
            # Or rob current house + best from two houses back (dp[i-2] + nums[i])
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]


# Space-Optimized Solution (O(1) space)
class SolutionOptimized:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev2 = nums[0]                  # dp[i-2]
        prev1 = max(nums[0], nums[1])    # dp[i-1]
        
        for i in range(2, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        
        return prev1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    optimized = SolutionOptimized()
    
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([1], 1),
        ([1, 2], 2),
        ([0, 0, 0], 0),
        ([400, 400, 400, 400], 800),
    ]
    
    print("=" * 55)
    print(f"{'Input':<25} {'Expected':<12} {'Got':<10} {'Status'}")
    print("=" * 55)
    
    for nums, expected in test_cases:
        result_dp = solution.rob(nums[:])
        result_opt = optimized.rob(nums[:])
        status = "✓ PASS" if result_dp == expected and result_opt == expected else "✗ FAIL"
        print(f"{str(nums):<25} {expected:<12} {result_dp:<10} {status}")
    
    print("=" * 55)