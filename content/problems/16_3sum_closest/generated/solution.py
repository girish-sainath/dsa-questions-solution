from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    """
    Find three integers in nums whose sum is closest to target.
    
    Args:
        nums: List of integers
        target: Target integer to approach
    
    Returns:
        The sum of three integers closest to target
    """
    # Sort array to enable two-pointer technique
    nums.sort()
    n = len(nums)
    
    # Initialize closest sum with the first three elements
    closest_sum = nums[0] + nums[1] + nums[2]
    
    # Fix the first element of the triplet
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        # Two pointer approach for the remaining two elements
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # Update closest_sum if current_sum is nearer to target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            # If exact match found, return immediately
            if current_sum == target:
                return current_sum
            elif current_sum < target:
                # Sum too small, move left pointer right to increase sum
                left += 1
            else:
                # Sum too large, move right pointer left to decrease sum
                right -= 1
    
    return closest_sum


# ============================================================
# Test Cases
# ============================================================
def run_tests():
    test_cases = [
        {
            "nums": [-1, 2, 1, -4],
            "target": 1,
            "expected": 2,
            "explanation": "(-1 + 2 + 1 = 2) is closest to 1"
        },
        {
            "nums": [0, 0, 0],
            "target": 1,
            "expected": 0,
            "explanation": "(0 + 0 + 0 = 0) is closest to 1"
        },
        {
            "nums": [1, 1, 1, 0],
            "target": -100,
            "expected": 2,
            "explanation": "All sums are positive, minimum is 1+1+0=2"
        },
        {
            "nums": [-100, -100, 0, 100, 100],
            "target": 0,
            "expected": 0,
            "explanation": "(-100 + 0 + 100 = 0) exactly matches target"
        },
        {
            "nums": [1, 2, 4, 8, 16, 32, 64, 128],
            "target": 82,
            "expected": 82,
            "explanation": "(2 + 16 + 64 = 82) exactly matches target"
        }
    ]
    
    print("=" * 60)
    print("Running Test Cases for 3Sum Closest")
    print("=" * 60)
    
    all_passed = True
    for i, tc in enumerate(test_cases, 1):
        result = threeSumClosest(tc["nums"], tc["target"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        
        if result != tc["expected"]:
            all_passed = False
        
        print(f"\nTest {i}: {status}")
        print(f"  Input:       nums={tc['nums']}, target={tc['target']}")
        print(f"  Expected:    {tc['expected']}")
        print(f"  Got:         {result}")
        print(f"  Explanation: {tc['explanation']}")
    
    print("\n" + "=" * 60)
    print("All tests passed! ✅" if all_passed else "Some tests failed! ❌")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()