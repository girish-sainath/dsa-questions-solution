import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find kth largest element using QuickSelect algorithm.
        
        Time Complexity: O(n) average, O(n²) worst case
        Space Complexity: O(1) - in-place partitioning
        """
        # Convert kth largest to index in sorted descending order
        # kth largest = (n - k)th smallest
        target = len(nums) - k
        
        def partition(left: int, right: int) -> int:
            """
            Partition array around a randomly chosen pivot.
            Returns the final position of the pivot.
            """
            # Random pivot to avoid worst case O(n²) for sorted arrays
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            
            pivot = nums[right]
            store_idx = left  # Position where pivot will ultimately be placed
            
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1
            
            # Place pivot in its correct position
            nums[store_idx], nums[right] = nums[right], nums[store_idx]
            return store_idx
        
        def quickselect(left: int, right: int) -> int:
            """
            Recursively find the target index element.
            """
            if left == right:
                return nums[left]
            
            pivot_pos = partition(left, right)
            
            if pivot_pos == target:
                return nums[pivot_pos]
            elif pivot_pos < target:
                # Target is in right portion
                return quickselect(pivot_pos + 1, right)
            else:
                # Target is in left portion
                return quickselect(left, pivot_pos - 1)
        
        return quickselect(0, len(nums) - 1)


# ============================================
# Alternative Approach: Min-Heap
# ============================================
import heapq

class SolutionHeap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find kth largest using a min-heap of size k.
        
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        # Maintain a min-heap of size k
        # The smallest element in heap = kth largest in array
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            # Keep heap size at k by removing smallest
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Root of min-heap is the kth largest
        return min_heap[0]


# ============================================
# Test Cases
# ============================================
def run_tests():
    solution = Solution()
    solution_heap = SolutionHeap()
    
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 6, 5, 4, 3, 2, 1], 1, 7),
        ([7, 6, 5, 4, 3, 2, 1], 7, 1),
        ([-1, -2, -3, -4, -5], 2, -2),
    ]
    
    print("=" * 55)
    print(f"{'Test':<5} {'Input':<30} {'k':<5} {'Expected':<10} {'QS':<8} {'Heap'}")
    print("=" * 55)
    
    all_passed = True
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result_qs = solution.findKthLargest(nums[:], k)   # copy since QuickSelect modifies array
        result_heap = solution_heap.findKthLargest(nums[:], k)
        
        qs_status = "✓" if result_qs == expected else "✗"
        heap_status = "✓" if result_heap == expected else "✗"
        
        print(f"{i:<5} {str(nums):<30} {k:<5} {expected:<10} {qs_status+str(result_qs):<8} {heap_status+str(result_heap)}")
        
        if result_qs != expected or result_heap != expected:
            all_passed = False
    
    print("=" * 55)
    print(f"All tests passed: {all_passed}")

run_tests()