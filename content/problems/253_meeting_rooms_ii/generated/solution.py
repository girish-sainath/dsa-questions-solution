import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Uses a min-heap to track the earliest ending meeting room.
        
        Algorithm:
        1. Sort intervals by start time
        2. Use a min-heap to store end times of ongoing meetings
        3. For each meeting:
           - If the earliest ending meeting has ended before current starts,
             reuse that room (pop from heap)
           - Otherwise, allocate a new room
        4. Heap size at the end = minimum rooms needed
        
        Time Complexity:  O(n log n) - sorting + heap operations
        Space Complexity: O(n) - heap storage
        """
        if not intervals:
            return 0
        
        # Sort meetings by start time
        intervals.sort(key=lambda x: x[0])
        
        # Min-heap to track end times of ongoing meetings
        # The root always contains the meeting that ends the earliest
        heap = []
        
        for start, end in intervals:
            if heap and heap[0] <= start:
                # The earliest-ending room is free, reuse it
                # Replace the old end time with the new meeting's end time
                heapq.heapreplace(heap, end)
            else:
                # No room is free, allocate a new room
                heapq.heappush(heap, end)
        
        # The number of rooms in use = size of heap
        return len(heap)


# ─────────────────────────────────────────────
# Test Cases
# ─────────────────────────────────────────────
def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "intervals": [[0, 30], [5, 10], [15, 20]],
            "expected": 2,
            "description": "Two overlapping meetings require 2 rooms"
        },
        {
            "intervals": [[7, 10], [2, 4]],
            "expected": 1,
            "description": "Non-overlapping meetings need only 1 room"
        },
        {
            "intervals": [[1, 5], [2, 6], [3, 7]],
            "expected": 3,
            "description": "Three simultaneous meetings need 3 rooms"
        },
        {
            "intervals": [[1, 10], [2, 3], [4, 5], [6, 7]],
            "expected": 2,
            "description": "Nested meetings - 2 rooms needed"
        },
        {
            "intervals": [[0, 5], [5, 10], [10, 15]],
            "expected": 1,
            "description": "Back-to-back meetings - 1 room (end == next start)"
        },
        {
            "intervals": [[1, 4]],
            "expected": 1,
            "description": "Single meeting needs 1 room"
        },
        {
            "intervals": [],
            "expected": 0,
            "description": "No meetings - 0 rooms needed"
        },
    ]
    
    print("=" * 60)
    print(f"{'Test':<5} {'Result':<10} {'Expected':<10} {'Status':<8} Description")
    print("=" * 60)
    
    for i, tc in enumerate(test_cases, 1):
        result = solution.minMeetingRooms(tc["intervals"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        print(f"{i:<5} {result:<10} {tc['expected']:<10} {status:<8} {tc['description']}")
    
    print("=" * 60)


if __name__ == "__main__":
    run_tests()