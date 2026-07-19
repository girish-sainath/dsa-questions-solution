from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Check if any permutation of s1 exists as a substring in s2.
        
        Args:
            s1: The pattern string
            s2: The string to search in
            
        Returns:
            True if s2 contains a permutation of s1, False otherwise
        """
        len1, len2 = len(s1), len(s2)
        
        # Edge case: s1 is longer than s2
        if len1 > len2:
            return False
        
        # Initialize frequency counts for s1 and the first window of s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])
        
        # Check if the first window matches
        if s1_count == window_count:
            return True
        
        # Slide the window across s2
        for i in range(len1, len2):
            # Add new character entering the window
            new_char = s2[i]
            window_count[new_char] += 1
            
            # Remove character leaving the window
            old_char = s2[i - len1]
            window_count[old_char] -= 1
            
            # Clean up zero counts to allow accurate comparison
            if window_count[old_char] == 0:
                del window_count[old_char]
            
            # Check if current window matches s1's frequency
            if s1_count == window_count:
                return True
        
        return False


# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("ab", "eidbaooo", True),   # "ba" is a permutation of "ab"
        ("ab", "eidboaoo", False),  # No permutation of "ab" in s2
        ("a", "a", True),           # Single char match
        ("abc", "bbbca", True),     # "bca" is a permutation
        ("hello", "ooolleoooleh", False),  # No valid permutation window
        ("adc", "dcda", True),      # "cda" or "dca" matches
    ]
    
    for i, (s1, s2, expected) in enumerate(test_cases):
        result = solution.checkInclusion(s1, s2)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i+1}: s1='{s1}', s2='{s2}' => {result} (Expected: {expected}) {status}")