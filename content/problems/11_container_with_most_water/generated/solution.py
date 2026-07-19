def maxArea(height):
    """
    Find the maximum water container using two pointer technique.
    
    Args:
        height: List of integers representing vertical line heights
    
    Returns:
        Maximum amount of water a container can store
    """
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        # Update maximum water
        max_water = max(max_water, current_area)
        
        # Move the pointer with the shorter line
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


# Test Cases
def run_tests():
    test_cases = [
        {
            "input": [1, 8, 6, 2, 5, 4, 8, 3, 7],
            "expected": 49,
            "description": "Standard case with multiple heights"
        },
        {
            "input": [1, 1],
            "expected": 1,
            "description": "Minimum case with two equal lines"
        },
        {
            "input": [4, 3, 2, 1, 4],
            "expected": 16,
            "description": "Same height at both ends"
        },
        {
            "input": [1, 2, 1],
            "expected": 2,
            "description": "Three elements"
        },
        {
            "input": [1, 8, 100, 2, 100, 4, 8, 3, 7],
            "expected": 200,
            "description": "Two tall lines in the middle"
        }
    ]
    
    print("=" * 55)
    print("Testing Container With Most Water")
    print("=" * 55)
    
    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result = maxArea(test["input"])
        status = "✅ PASS" if result == test["expected"] else "❌ FAIL"
        
        if result != test["expected"]:
            all_passed = False
        
        print(f"\nTest {i}: {test['description']}")
        print(f"  Input:    {test['input']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}")
    
    print("\n" + "=" * 55)
    print(f"Overall: {'All tests passed! 🎉' if all_passed else 'Some tests failed! ❌'}")
    print("=" * 55)


run_tests()