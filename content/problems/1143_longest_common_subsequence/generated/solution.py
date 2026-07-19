from typing import List
from collections import defaultdict

def smallestCommonElement(mat: List[List[int]]) -> int:
    """
    Find the smallest common element in all rows of the matrix.
    
    Args:
        mat: m x n matrix where every row is sorted in strictly increasing order
        
    Returns:
        Smallest common element, or -1 if none exists
    """
    m = len(mat)       # number of rows
    n = len(mat[0])    # number of columns
    
    # Count frequency of each element across all rows
    count = defaultdict(int)
    
    for row in mat:
        for num in row:
            count[num] += 1
            # Early termination: if element appears in all rows, return it
            # Since rows are sorted, we process in increasing order per row
            # but we need the global minimum, so we check after counting all
    
    # Find the smallest element with frequency equal to m (number of rows)
    # Iterate through first row (sorted) to find smallest common element efficiently
    for num in mat[0]:
        if count[num] == m:
            return num
    
    return -1


# Alternative Method: Binary Search
def smallestCommonElementBinarySearch(mat: List[List[int]]) -> int:
    """
    Find the smallest common element using binary search.
    
    For each element in the first row, binary search for it in all other rows.
    Since first row is sorted, the first match found will be the smallest.
    
    Time Complexity: O(m * n * log(n))
    Space Complexity: O(1)
    """
    import bisect
    
    m = len(mat)
    n = len(mat[0])
    
    # Iterate through first row (sorted ascending)
    for num in mat[0]:
        found_in_all = True
        
        # Binary search for num in every other row
        for i in range(1, m):
            pos = bisect.bisect_left(mat[i], num)
            # Check if num exists at the found position
            if pos == n or mat[i][pos] != num:
                found_in_all = False
                break
        
        if found_in_all:
            return num
    
    return -1


# Test cases
def run_tests():
    test_cases = [
        {
            "mat": [
                [1, 2, 3, 4, 5],
                [2, 4, 5, 8, 10],
                [3, 5, 7, 9, 11],
                [1, 3, 5, 7, 9]
            ],
            "expected": 5
        },
        {
            "mat": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            "expected": -1
        },
        {
            "mat": [
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5]
            ],
            "expected": 1
        },
        {
            "mat": [
                [1, 10, 100],
                [1, 10, 100],
                [1, 10, 100]
            ],
            "expected": 1
        },
        {
            "mat": [
                [5]
            ],
            "expected": 5
        }
    ]
    
    print("=" * 60)
    print("Testing HashMap Approach:")
    print("=" * 60)
    for i, tc in enumerate(test_cases):
        result = smallestCommonElement(tc["mat"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        print(f"Test {i+1}: {status} | Result: {result} | Expected: {tc['expected']}")
    
    print()
    print("=" * 60)
    print("Testing Binary Search Approach:")
    print("=" * 60)
    for i, tc in enumerate(test_cases):
        result = smallestCommonElementBinarySearch(tc["mat"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        print(f"Test {i+1}: {status} | Result: {result} | Expected: {tc['expected']}")


if __name__ == "__main__":
    run_tests()