import heapq

class MedianFinder:
    """
    Uses two heaps to efficiently find median from a data stream.
    
    - small: max-heap (inverted min-heap) for lower half
    - large: min-heap for upper half
    
    Invariant: len(small) >= len(large), and len(small) - len(large) <= 1
    """
    
    def __init__(self):
        # Max-heap for lower half (negate values for max-heap simulation)
        self.small = []  # max-heap (stores negatives)
        # Min-heap for upper half
        self.large = []  # min-heap
    
    def addNum(self, num: int) -> None:
        """
        Add number to appropriate heap and rebalance if necessary.
        Time: O(log n)
        """
        # Step 1: Always push to max-heap first
        heapq.heappush(self.small, -num)
        
        # Step 2: Ensure max of small <= min of large
        # (every element in small must be <= every element in large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Step 3: Rebalance sizes
        # small can have at most 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def findMedian(self) -> float:
        """
        Return median of all elements.
        Time: O(1)
        """
        # Odd total: small has one more element (the median)
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        
        # Even total: average of tops of both heaps
        return (-self.small[0] + self.large[0]) / 2.0


# ============================================================
# Testing
# ============================================================
def run_tests():
    print("=" * 50)
    print("Test 1: Basic Example")
    print("=" * 50)
    mf = MedianFinder()
    mf.addNum(1)
    print(f"Added 1, arr = [1]")
    mf.addNum(2)
    print(f"Added 2, arr = [1, 2]")
    median = mf.findMedian()
    print(f"findMedian() = {median} (expected: 1.5)")
    
    mf.addNum(3)
    print(f"Added 3, arr = [1, 2, 3]")
    median = mf.findMedian()
    print(f"findMedian() = {median} (expected: 2.0)")
    
    print("\n" + "=" * 50)
    print("Test 2: Single Element")
    print("=" * 50)
    mf2 = MedianFinder()
    mf2.addNum(5)
    print(f"Added 5, arr = [5]")
    print(f"findMedian() = {mf2.findMedian()} (expected: 5.0)")
    
    print("\n" + "=" * 50)
    print("Test 3: Negative Numbers")
    print("=" * 50)
    mf3 = MedianFinder()
    for num in [-5, -3, -1, -4, -2]:
        mf3.addNum(num)
    print(f"Added [-5, -3, -1, -4, -2], sorted = [-5, -4, -3, -2, -1]")
    print(f"findMedian() = {mf3.findMedian()} (expected: -3.0)")
    
    print("\n" + "=" * 50)
    print("Test 4: Mixed Numbers")
    print("=" * 50)
    mf4 = MedianFinder()
    nums = [6, 1, 4, 2, 9, 7]
    for num in nums:
        mf4.addNum(num)
    print(f"Added {nums}, sorted = {sorted(nums)}")
    print(f"findMedian() = {mf4.findMedian()} (expected: {(4+6)/2})")
    
    print("\n" + "=" * 50)
    print("Test 5: Step-by-step medians")
    print("=" * 50)
    mf5 = MedianFinder()
    stream = [5, 15, 1, 3, 8]
    for num in stream:
        mf5.addNum(num)
        print(f"Added {num} -> median = {mf5.findMedian()}")

run_tests()