from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        
        # Binary search on nums1
        low, high = 0, m
        
        while low <= high:
            # i = partition index for nums1 (number of elements from nums1 on the left)
            i = (low + high) // 2
            # j = partition index for nums2 (number of elements from nums2 on the left)
            j = half_len - i
            
            # Get boundary values (use -inf/+inf for edge cases)
            nums1_left_max  = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf')  if i == m else nums1[i]
            nums2_left_max  = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf')  if j == n else nums2[j]
            
            # Check if partition is valid
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Found the correct partition
                max_left  = max(nums1_left_max, nums2_left_max)
                min_right = min(nums1_right_min, nums2_right_min)
                
                # Return median based on total length
                if (m + n) % 2 == 1:
                    return float(max_left)
                else:
                    return (max_left + min_right) / 2.0
            
            elif nums1_left_max > nums2_right_min:
                # Move partition in nums1 to the left
                high = i - 1
            else:
                # Move partition in nums1 to the right
                low = i + 1
        
        raise ValueError("Input arrays are not sorted!")


# ─────────────────────────────────────────────
# Test Cases
# ─────────────────────────────────────────────
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, 3],    [2],       2.00000),
        ([1, 2],    [3, 4],    2.50000),
        ([0, 0],    [0, 0],    0.00000),
        ([],        [1],       1.00000),
        ([2],       [],        2.00000),
        ([1,2,3,4], [5,6,7,8], 4.50000),
    ]
    
    for i, (nums1, nums2, expected) in enumerate(test_cases, 1):
        result = solution.findMedianSortedArrays(nums1, nums2)
        status = "✅ PASS" if abs(result - expected) < 1e-5 else "❌ FAIL"
        print(f"Test {i}: nums1={nums1}, nums2={nums2}")
        print(f"         Expected={expected:.5f}, Got={result:.5f} → {status}\n")