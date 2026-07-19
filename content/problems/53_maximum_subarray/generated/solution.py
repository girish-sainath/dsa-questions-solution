from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the maximum sum subarray using Kadane's Algorithm.
        
        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum sum of any subarray
        """
        # Initialize current sum and max sum with the first element
        current_sum = nums[0]
        max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If current_sum is negative, start a new subarray from current element
            # Otherwise, extend the existing subarray
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    def maxSubArrayDivideConquer(self, nums: List[int]) -> int:
        """
        Find the maximum sum subarray using Divide and Conquer approach.
        
        Time Complexity: O(n log n) - dividing array in half each time
        Space Complexity: O(log n) - recursion stack
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum sum of any subarray
        """
        def helper(left: int, right: int) -> int:
            # Base case: single element
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            # Find max sum in left half
            left_max = helper(left, mid)
            
            # Find max sum in right half
            right_max = helper(mid + 1, right)
            
            # Find max sum crossing the middle
            cross_max = crossSum(left, right, mid)
            
            return max(left_max, right_max, cross_max)
        
        def crossSum(left: int, right: int, mid: int) -> int:
            # Find max sum extending from mid to left
            left_sum = float('-inf')
            current = 0
            for i in range(mid, left - 1, -1):
                current += nums[i]
                left_sum = max(left_sum, current)
            
            # Find max sum extending from mid+1 to right
            right_sum = float('-inf')
            current = 0
            for i in range(mid + 1, right + 1):
                current += nums[i]
                right_sum = max(right_sum, current)
            
            return left_sum + right_sum
        
        return helper(0, len(nums) - 1)


# ==================== Test Cases ====================
def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            "expected": 6,
            "explanation": "Subarray [4,-1,2,1] has the largest sum 6"
        },
        {
            "nums": [1],
            "expected": 1,
            "explanation": "Single element [1] has the largest sum 1"
        },
        {
            "nums": [5, 4, -1, 7, 8],
            "expected": 23,
            "explanation": "Entire array [5,4,-1,7,8] has the largest sum 23"
        },
        {
            "nums": [-1, -2, -3, -4],
            "expected": -1,
            "explanation": "All negative: best is the least negative [-1]"
        },
        {
            "nums": [-2, -1],
            "expected": -1,
            "explanation": "All negative: best is the least negative [-1]"
        }
    ]
    
    print("=" * 60)
    print("Testing Kadane's Algorithm (O(n))")
    print("=" * 60)
    for i, tc in enumerate(test_cases, 1):
        result = solution.maxSubArray(tc["nums"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        print(f"Test {i}: {status}")
        print(f"  Input:       {tc['nums']}")
        print(f"  Expected:    {tc['expected']}")
        print(f"  Got:         {result}")
        print(f"  Explanation: {tc['explanation']}")
        print()
    
    print("=" * 60)
    print("Testing Divide and Conquer (O(n log n))")
    print("=" * 60)
    for i, tc in enumerate(test_cases, 1):
        result = solution.maxSubArrayDivideConquer(tc["nums"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        print(f"Test {i}: {status}")
        print(f"  Input:       {tc['nums']}")
        print(f"  Expected:    {tc['expected']}")
        print(f"  Got:         {result}")
        print(f"  Explanation: {tc['explanation']}")
        print()


if __name__ == "__main__":
    run_tests()