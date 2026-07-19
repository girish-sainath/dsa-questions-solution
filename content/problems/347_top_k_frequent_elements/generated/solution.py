from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies of each number
        # Time: O(n), Space: O(n)
        freq_map = Counter(nums)
        
        # Step 2: Create buckets where index represents frequency
        # bucket[i] contains all numbers that appear exactly i times
        # Max frequency can be len(nums), so we need len(nums) + 1 buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # Step 3: Collect top k frequent elements
        # Iterate from highest frequency to lowest
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result


# ============================================================
# Test Cases
# ============================================================
def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "nums": [1, 1, 1, 2, 2, 3],
            "k": 2,
            "expected": [1, 2],
            "description": "Basic case with 3 unique elements"
        },
        {
            "nums": [1],
            "k": 1,
            "expected": [1],
            "description": "Single element"
        },
        {
            "nums": [1, 2, 1, 2, 1, 2, 3, 1, 3, 2],
            "k": 2,
            "expected": [1, 2],
            "description": "Tied frequencies"
        },
        {
            "nums": [4, 1, -1, 2, -1, 2, 3],
            "k": 2,
            "expected": [-1, 2],
            "description": "Contains negative numbers"
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 3,
            "expected": [1, 2, 3],  # Any 3 elements (all freq = 1)
            "description": "All elements have same frequency"
        }
    ]
    
    print("=" * 60)
    print("Testing Top K Frequent Elements")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        nums = test["nums"]
        k = test["k"]
        expected = test["expected"]
        result = solution.topKFrequent(nums, k)
        
        # Since order doesn't matter, compare as sets
        passed = set(result) == set(expected)
        
        print(f"\nTest {i}: {test['description']}")
        print(f"  Input:    nums={nums}, k={k}")
        print(f"  Expected: {sorted(expected)}")
        print(f"  Got:      {sorted(result)}")
        print(f"  Status:   {'✅ PASSED' if passed else '❌ FAILED'}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    run_tests()