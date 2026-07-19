def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without duplicate characters
    """
    # Dictionary to store the last seen index of each character
    char_index = {}
    
    max_length = 0
    left = 0  # Left pointer of the sliding window
    
    for right, char in enumerate(s):
        # If character is seen and its last occurrence is within the current window
        if char in char_index and char_index[char] >= left:
            # Move left pointer past the previous occurrence of this character
            left = char_index[char] + 1
        
        # Update the last seen index of current character
        char_index[char] = right
        
        # Update max length if current window is larger
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ─────────────────────────────────────────────
# Test Cases
# ─────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),   # "abc", "bca", or "cab"
        ("bbbbb",    1),   # "b"
        ("pwwkew",   3),   # "wke"
        ("",         0),   # empty string
        (" ",        1),   # single space
        ("dvdf",     3),   # "vdf"
        ("abcdef",   6),   # all unique
        ("aab",      2),   # "ab"
    ]
    
    print(f"{'Input':<15} {'Expected':<10} {'Got':<10} {'Status'}")
    print("─" * 50)
    
    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"{repr(s):<15} {expected:<10} {result:<10} {status}")