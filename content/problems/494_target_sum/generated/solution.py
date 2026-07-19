from typing import List
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Uses memoized recursion (top-down DP) to count expressions
        that evaluate to target.
        
        Time Complexity: O(n * total_sum) where n is len(nums)
        Space Complexity: O(n * total_sum) for memoization cache
        """
        
        @lru_cache(maxsize=None)
        def dp(index: int, current_sum: int) -> int:
            # Base case: processed all numbers
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            # Choice 1: Add current number
            add = dp(index + 1, current_sum + nums[index])
            
            # Choice 2: Subtract current number
            subtract = dp(index + 1, current_sum - nums[index])
            
            return add + subtract
        
        return dp(0, 0)


class SolutionDP:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Bottom-up DP approach using dictionary to track possible sums.
        
        At each step, maintains a dict of {current_sum: count_of_ways}
        
        Time Complexity: O(n * total_sum)
        Space Complexity: O(total_sum)
        """
        # dp dict: {current_sum: number_of_ways_to_reach_it}
        dp = {0: 1}
        
        for num in nums:
            new_dp = {}
            for current_sum, count in dp.items():
                # Add current number
                new_sum_add = current_sum + num
                new_dp[new_sum_add] = new_dp.get(new_sum_add, 0) + count
                
                # Subtract current number
                new_sum_sub = current_sum - num
                new_dp[new_sum_sub] = new_dp.get(new_sum_sub, 0) + count
            
            dp = new_dp
        
        return dp.get(target, 0)


# ============ TEST CASES ============
def run_tests():
    solution1 = Solution()
    solution2 = SolutionDP()
    
    test_cases = [
        {
            "nums": [1, 1, 1, 1, 1],
            "target": 3,
            "expected": 5,
            "description": "Five ones with target 3"
        },
        {
            "nums": [1],
            "target": 1,
            "expected": 1,
            "description": "Single element equals target"
        },
        {
            "nums": [1],
            "target": 2,
            "expected": 0,
            "description": "Target unreachable"
        },
        {
            "nums": [0, 0, 0, 0, 0],
            "target": 0,
            "expected": 32,
            "description": "All zeros - each can be + or -, 2^5 = 32 ways"
        },
        {
            "nums": [1, 2, 3],
            "target": 0,
            "expected": 2,
            "description": "Target zero: +1-2+1 invalid, -1+2-3? No: +1+2-3=0, -1-2+3=0"
        }
    ]
    
    print("=" * 60)
    print("Testing Target Sum Solutions")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        nums = test["nums"]
        target = test["target"]
        expected = test["expected"]
        
        result1 = solution1.findTargetSumWays(nums, target)
        result2 = solution2.findTargetSumWays(nums, target)
        
        status1 = "✓ PASS" if result1 == expected else "✗ FAIL"
        status2 = "✓ PASS" if result2 == expected else "✗ FAIL"
        
        print(f"\nTest {i}: {test['description']}")
        print(f"  Input:    nums={nums}, target={target}")
        print(f"  Expected: {expected}")
        print(f"  Memoized: {result1} {status1}")
        print(f"  Bottom-Up: {result2} {status2}")

if __name__ == "__main__":
    run_tests()