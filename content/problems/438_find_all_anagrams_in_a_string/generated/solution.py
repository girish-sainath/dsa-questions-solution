from collections import Counter
from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    """
    Find all start indices of p's anagrams in s using sliding window approach.
    
    Args:
        s: The main string to search in
        p: The pattern string to find anagrams of
        
    Returns:
        List of start indices where anagrams of p begin in s
    """
    result = []
    
    # Edge case: if p is longer than s, no anagrams possible
    if len(p) > len(s):
        return result
    
    p_count = Counter(p)          # Frequency count of p
    window_count = Counter(s[:len(p)])  # Frequency count of initial window
    
    # Check if initial window is an anagram
    if window_count == p_count:
        result.append(0)
    
    # Slide the window across s
    for i in range(len(p), len(s)):
        # Add new character to window
        new_char = s[i]
        window_count[new_char] += 1
        
        # Remove the character that's leaving the window
        old_char = s[i - len(p)]
        window_count[old_char] -= 1
        
        # Clean up zero counts to ensure accurate comparison
        if window_count[old_char] == 0:
            del window_count[old_char]
        
        # Check if current window is an anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result


# Test cases
if __name__ == "__main__":
    # Example 1
    s1, p1 = "cbaebabacd", "abc"
    output1 = findAnagrams(s1, p1)
    print(f"Input: s = '{s1}', p = '{p1}'")
    print(f"Output: {output1}")
    print(f"Expected: [0, 6]\n")
    
    # Example 2
    s2, p2 = "abab", "ab"
    output2 = findAnagrams(s2, p2)
    print(f"Input: s = '{s2}', p = '{p2}'")
    print(f"Output: {output2}")
    print(f"Expected: [0, 1, 2]\n")
    
    # Edge case: p longer than s
    s3, p3 = "ab", "abc"
    output3 = findAnagrams(s3, p3)
    print(f"Input: s = '{s3}', p = '{p3}'")
    print(f"Output: {output3}")
    print(f"Expected: []\n")
    
    # Edge case: exact match
    s4, p4 = "abc", "abc"
    output4 = findAnagrams(s4, p4)
    print(f"Input: s = '{s4}', p = '{p4}'")
    print(f"Output: {output4}")
    print(f"Expected: [0]")