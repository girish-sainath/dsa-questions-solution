def missingNumber(nums):
    """
    Find the missing number in range [0, n].
    
    Args:
        nums: List of n distinct numbers in range [0, n]
    
    Returns:
        The missing number
    
    Time Complexity: O(n) - single pass to compute sum
    Space Complexity: O(1) - only constant extra space
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Gauss formula: sum of 0 to n
    actual_sum = sum(nums)            # sum of given numbers
    return expected_sum - actual_sum


# ─── Test Cases ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    test_cases = [
        {"nums": [3, 0, 1],             "expected": 2},
        {"nums": [0, 1],                "expected": 2},
        {"nums": [9,6,4,2,3,5,7,0,1],  "expected": 8},
        {"nums": [0],                   "expected": 1},  # single element, missing 1
        {"nums": [1],                   "expected": 0},  # single element, missing 0
    ]

    for i, tc in enumerate(test_cases, 1):
        result = missingNumber(tc["nums"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        print(f"Test {i}: {status} | nums={tc['nums']} | "
              f"expected={tc['expected']}, got={result}")