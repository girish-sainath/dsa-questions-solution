import bisect
from typing import List

class Solution:
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        """
        Dynamic Programming approach - O(n^2) time, O(n) space
        dp[i] = length of LIS ending at index i
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n  # Every element is an LIS of length 1 by itself
        
        for i in range(1, n):
            for j in range(i):
                # If nums[j] < nums[i], we can extend the subsequence ending at j
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Binary Search (Patience Sorting) approach - O(n log n) time, O(n) space
        tails[i] = smallest tail element of all LIS of length i+1
        """
        if not nums:
            return 0
        
        tails = []  # Stores the smallest tail for each length of LIS
        
        for num in nums:
            # Find the leftmost position in tails where tails[pos] >= num
            pos = bisect.bisect_left(tails, num)
            
            if pos == len(tails):
                # num is larger than all tails, extend the longest subsequence
                tails.append(num)
            else:
                # Replace the first tail that is >= num
                # This maintains the smallest possible tail for length pos+1
                tails[pos] = num
        
        # Length of tails array = length of LIS
        return len(tails)


# ==================== Test Cases ====================
def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "nums": [10, 9, 2, 5, 3, 7, 101, 18],
            "expected": 4,
            "explanation": "LIS is [2, 3, 7, 101]"
        },
        {
            "nums": [0, 1, 0, 3, 2, 3],
            "expected": 4,
            "explanation": "LIS is [0, 1, 2, 3]"
        },
        {
            "nums": [7, 7, 7, 7, 7, 7, 7],
            "expected": 1,
            "explanation": "All elements are equal, LIS length is 1"
        },
        {
            "nums": [1],
            "expected": 1,
            "explanation": "Single element"
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "expected": 5,
            "explanation": "Already sorted, LIS is entire array"
        },
        {
            "nums": [5, 4, 3, 2, 1],
            "expected": 1,
            "explanation": "Reverse sorted, LIS length is 1"
        }
    ]
    
    print("=" * 60)
    print("Testing Longest Increasing Subsequence")
    print("=" * 60)
    
    all_passed = True
    
    for i, tc in enumerate(test_cases, 1):
        nums = tc["nums"]
        expected = tc["expected"]
        
        result_dp = solution.lengthOfLIS_dp(nums)
        result_bs = solution.lengthOfLIS(nums)
        
        status_dp = "✅ PASS" if result_dp == expected else "❌ FAIL"
        status_bs = "✅ PASS" if result_bs == expected else "❌ FAIL"
        
        if result_dp != expected or result_bs != expected:
            all_passed = False
        
        print(f"\nTest Case {i}: {tc['explanation']}")
        print(f"  Input:           {nums}")
        print(f"  Expected:        {expected}")
        print(f"  DP Result:       {result_dp} {status_dp}")
        print(f"  BinSearch Result:{result_bs} {status_bs}")
    
    print("\n" + "=" * 60)
    print("All tests passed! ✅" if all_passed else "Some tests failed! ❌")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()