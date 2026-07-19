from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations of candidates that sum to target.
    
    Args:
        candidates: List of distinct integers to choose from
        target: Target sum to achieve
        
    Returns:
        List of all unique combinations that sum to target
    """
    result = []
    candidates.sort()  # Sort to enable early pruning
    
    def backtrack(start: int, current_combination: List[int], current_sum: int):
        """
        Recursive backtracking function.
        
        Args:
            start: Starting index in candidates to avoid duplicate combinations
            current_combination: Current combination being built
            current_sum: Current sum of elements in combination
        """
        # Base case: found a valid combination
        if current_sum == target:
            result.append(current_combination[:])  # Add a copy of current combination
            return
        
        # Explore candidates starting from 'start' index
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            
            # Pruning: since array is sorted, no need to explore further
            if current_sum + candidate > target:
                break
            
            # Choose: add candidate to combination
            current_combination.append(candidate)
            
            # Explore: recurse with same index 'i' (can reuse same element)
            backtrack(i, current_combination, current_sum + candidate)
            
            # Unchoose: remove candidate (backtrack)
            current_combination.pop()
    
    backtrack(0, [], 0)
    return result


# ==================== Test Cases ====================

def run_tests():
    test_cases = [
        {
            "candidates": [2, 3, 6, 7],
            "target": 7,
            "expected": [[2, 2, 3], [7]],
            "description": "Example 1: Multiple combinations"
        },
        {
            "candidates": [2, 3, 5],
            "target": 8,
            "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            "description": "Example 2: Three combinations"
        },
        {
            "candidates": [2],
            "target": 1,
            "expected": [],
            "description": "Example 3: No valid combination"
        },
        {
            "candidates": [2],
            "target": 4,
            "expected": [[2, 2]],
            "description": "Single candidate repeated"
        },
        {
            "candidates": [5, 10, 15],
            "target": 20,
            "expected": [[5, 5, 5, 5], [5, 5, 10], [5, 15], [10, 10]],
            "description": "Multiple ways with larger numbers"
        }
    ]
    
    all_passed = True
    
    for i, test in enumerate(test_cases, 1):
        candidates = test["candidates"]
        target = test["target"]
        expected = test["expected"]
        
        result = combinationSum(candidates[:], target)  # Pass copy to preserve original
        
        # Sort both for comparison (order doesn't matter)
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        status = "✅ PASSED" if result_sorted == expected_sorted else "❌ FAILED"
        if result_sorted != expected_sorted:
            all_passed = False
        
        print(f"Test {i}: {status}")
        print(f"  Description: {test['description']}")
        print(f"  Input: candidates={candidates}, target={target}")
        print(f"  Expected: {expected_sorted}")
        print(f"  Got:      {result_sorted}")
        print()
    
    print("=" * 40)
    print(f"All tests passed: {all_passed}")


if __name__ == "__main__":
    run_tests()