from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Returns minimum number of intervals to remove to make rest non-overlapping.
        
        Args:
            intervals: List of [start, end] intervals
            
        Returns:
            Minimum number of intervals to remove
        """
        if not intervals:
            return 0
        
        # Sort intervals by end time (greedy choice)
        intervals.sort(key=lambda x: x[1])
        
        # Track how many intervals we can KEEP (non-overlapping)
        count = 1  # Always keep the first interval (earliest end time)
        prev_end = intervals[0][1]  # End time of last kept interval
        
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            
            # If current interval starts at or after prev end -> no overlap
            # Note: touching at a point is allowed (curr_start >= prev_end)
            if curr_start >= prev_end:
                count += 1          # Keep this interval
                prev_end = curr_end  # Update the end time
            # else: overlap -> skip this interval (implicitly remove it)
        
        # Minimum removals = total - maximum we can keep
        return len(intervals) - count


# ============================================================
# Test Cases
# ============================================================
def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "intervals": [[1, 2], [2, 3], [3, 4], [1, 3]],
            "expected": 1,
            "explanation": "[1,3] can be removed"
        },
        {
            "intervals": [[1, 2], [1, 2], [1, 2]],
            "expected": 2,
            "explanation": "Remove two [1,2]"
        },
        {
            "intervals": [[1, 2], [2, 3]],
            "expected": 0,
            "explanation": "Already non-overlapping (touching at point)"
        },
        {
            "intervals": [[1, 100], [11, 22], [1, 11], [2, 12]],
            "expected": 2,
            "explanation": "Keep [1,11] and [11,22], remove others"
        },
        {
            "intervals": [[1, 2]],
            "expected": 0,
            "explanation": "Single interval, nothing to remove"
        },
    ]
    
    print("=" * 60)
    print("Testing Non-overlapping Intervals")
    print("=" * 60)
    
    all_passed = True
    for i, tc in enumerate(test_cases, 1):
        result = solution.eraseOverlapIntervals(tc["intervals"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        
        if result != tc["expected"]:
            all_passed = False
        
        print(f"\nTest {i}: {status}")
        print(f"  Input:       {tc['intervals']}")
        print(f"  Expected:    {tc['expected']}")
        print(f"  Got:         {result}")
        print(f"  Explanation: {tc['explanation']}")
    
    print("\n" + "=" * 60)
    print("All tests passed! ✅" if all_passed else "Some tests failed! ❌")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()