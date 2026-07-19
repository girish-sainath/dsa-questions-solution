def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge all overlapping intervals.
    
    Args:
        intervals: List of intervals [start, end]
    
    Returns:
        List of merged non-overlapping intervals
    """
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    
    for interval in intervals:
        # If merged is empty OR current interval doesn't overlap with previous
        # (current start > previous end), simply append
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Overlap exists, merge by updating the end of last interval
            # Take the maximum end to cover both intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged


# ==================== TEST CASES ====================

def run_tests():
    test_cases = [
        {
            "input": [[1,3],[2,6],[8,10],[15,18]],
            "expected": [[1,6],[8,10],[15,18]],
            "description": "Basic overlapping intervals"
        },
        {
            "input": [[1,4],[4,5]],
            "expected": [[1,5]],
            "description": "Touching intervals (boundary overlap)"
        },
        {
            "input": [[4,7],[1,4]],
            "expected": [[1,7]],
            "description": "Unsorted overlapping intervals"
        },
        {
            "input": [[1,4]],
            "expected": [[1,4]],
            "description": "Single interval"
        },
        {
            "input": [[1,4],[2,3]],
            "expected": [[1,4]],
            "description": "One interval completely inside another"
        },
        {
            "input": [[1,2],[3,4],[5,6]],
            "expected": [[1,2],[3,4],[5,6]],
            "description": "No overlapping intervals"
        }
    ]
    
    print("=" * 55)
    print("         MERGE INTERVALS - TEST RESULTS")
    print("=" * 55)
    
    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result = merge(test["input"].copy())  # Use copy to avoid mutation
        passed = result == test["expected"]
        all_passed = all_passed and passed
        status = "✅ PASS" if passed else "❌ FAIL"
        
        print(f"\nTest {i}: {test['description']}")
        print(f"  Input:    {test['input']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}")
    
    print("\n" + "=" * 55)
    print(f"  Final Result: {'✅ All Tests Passed!' if all_passed else '❌ Some Tests Failed!'}")
    print("=" * 55)

run_tests()