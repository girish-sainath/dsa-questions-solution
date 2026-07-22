from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        """
        Count groups of special-equivalent strings.
        
        Two strings are special-equivalent if their even-indexed characters
        form the same multiset AND their odd-indexed characters form the same multiset.
        
        Args:
            words: List of strings of the same length
            
        Returns:
            Number of groups of special-equivalent strings
        """
        signatures = set()
        
        for word in words:
            # Extract and sort even-indexed characters
            even_chars = sorted(word[i] for i in range(0, len(word), 2))
            
            # Extract and sort odd-indexed characters
            odd_chars = sorted(word[i] for i in range(1, len(word), 2))
            
            # Create a unique signature as a tuple of tuples
            signature = (tuple(even_chars), tuple(odd_chars))
            
            signatures.add(signature)
        
        return len(signatures)


# Test cases
def main():
    solution = Solution()
    
    # Test Case 1
    words1 = ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
    result1 = solution.numSpecialEquivGroups(words1)
    print(f"Input: {words1}")
    print(f"Output: {result1}")
    print(f"Expected: 3")
    print()
    
    # Test Case 2
    words2 = ["abc", "acb", "bac", "bca", "cab", "cba"]
    result2 = solution.numSpecialEquivGroups(words2)
    print(f"Input: {words2}")
    print(f"Output: {result2}")
    print(f"Expected: 3")
    print()
    
    # Additional Test Case - Single word
    words3 = ["hello"]
    result3 = solution.numSpecialEquivGroups(words3)
    print(f"Input: {words3}")
    print(f"Output: {result3}")
    print(f"Expected: 1")
    print()
    
    # Additional Test Case - All same words
    words4 = ["aa", "aa", "aa"]
    result4 = solution.numSpecialEquivGroups(words4)
    print(f"Input: {words4}")
    print(f"Output: {result4}")
    print(f"Expected: 1")

if __name__ == "__main__":
    main()