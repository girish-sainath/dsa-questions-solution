def longestPalindrome(s: str) -> str:
    """
    Find the longest palindromic substring using expand around center approach.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s or len(s) == 1:
        return s
    
    start = 0  # Start index of longest palindrome
    max_len = 1  # Length of longest palindrome
    
    def expand_around_center(left: int, right: int) -> tuple:
        """
        Expand outward from center indices while characters match.
        
        Args:
            left:  Left boundary index
            right: Right boundary index
            
        Returns:
            Tuple of (start_index, length) of the palindrome found
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # left+1 is actual start, right-1 is actual end
        palindrome_start = left + 1
        palindrome_length = right - left - 1
        return palindrome_start, palindrome_length
    
    for i in range(len(s)):
        # Case 1: Odd length palindrome (single character center)
        odd_start, odd_len = expand_around_center(i, i)
        
        # Case 2: Even length palindrome (two character center)
        even_start, even_len = expand_around_center(i, i + 1)
        
        # Update if odd palindrome is longer
        if odd_len > max_len:
            start = odd_start
            max_len = odd_len
        
        # Update if even palindrome is longer
        if even_len > max_len:
            start = even_start
            max_len = even_len
    
    return s[start : start + max_len]


# -------------------------
# Test Cases
# -------------------------
test_cases = [
    ("babad", ["bab", "aba"]),   # Multiple valid answers
    ("cbbd",  ["bb"]),
    ("a",     ["a"]),            # Single character
    ("ac",    ["a", "c"]),       # No palindrome longer than 1
    ("racecar", ["racecar"]),    # Entire string is palindrome
    ("aacabdkacaa", ["aca"]),    # Palindrome in middle
]

print("=" * 50)
print("Longest Palindromic Substring Tests")
print("=" * 50)

for s, expected_list in test_cases:
    result = longestPalindrome(s)
    passed = result in expected_list
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"{status} | Input: {s!r:15} | Output: {result!r:10} | Expected: {expected_list}")