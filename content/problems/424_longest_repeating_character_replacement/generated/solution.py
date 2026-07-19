def characterReplacement(s: str, k: int) -> int:
    """
    Find the longest substring with at most k character replacements
    to make all characters the same.
    
    Args:
        s: Input string of uppercase English letters
        k: Maximum number of character replacements allowed
    
    Returns:
        Length of the longest valid substring
    """
    char_count = {}  # Frequency map for current window
    max_freq = 0     # Maximum frequency of any single character in window
    left = 0         # Left pointer of sliding window
    max_length = 0   # Result: maximum valid window length
    
    for right in range(len(s)):
        # Add current character to window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update max frequency in current window
        max_freq = max(max_freq, char_count[s[right]])
        
        # Current window size
        window_size = right - left + 1
        
        # Check if window is valid: characters to replace <= k
        # characters_to_replace = window_size - max_freq
        if window_size - max_freq > k:
            # Shrink window from the left
            char_count[s[left]] -= 1
            left += 1
        
        # Update maximum length (window size after potential shrink)
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
if __name__ == "__main__":
    # Example 1
    s1, k1 = "ABAB", 2
    result1 = characterReplacement(s1, k1)
    print(f"Input: s = '{s1}', k = {k1}")
    print(f"Output: {result1}")  # Expected: 4
    print()
    
    # Example 2
    s2, k2 = "AABABBA", 1
    result2 = characterReplacement(s2, k2)
    print(f"Input: s = '{s2}', k = {k2}")
    print(f"Output: {result2}")  # Expected: 4
    print()
    
    # Edge cases
    s3, k3 = "AAAA", 2
    result3 = characterReplacement(s3, k3)
    print(f"Input: s = '{s3}', k = {k3}")
    print(f"Output: {result3}")  # Expected: 4
    print()
    
    s4, k4 = "ABCDE", 1
    result4 = characterReplacement(s4, k4)
    print(f"Input: s = '{s4}', k = {k4}")
    print(f"Output: {result4}")  # Expected: 2