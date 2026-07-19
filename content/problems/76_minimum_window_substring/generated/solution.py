from collections import Counter

def minWindow(s: str, t: str) -> str:
    """
    Find minimum window substring of s that contains all characters of t.
    
    Args:
        s: Source string to search in
        t: Target string whose characters must be in window
        
    Returns:
        Minimum window substring, or "" if no valid window exists
    """
    if not s or not t:
        return ""
    
    # Frequency map for characters in t
    t_count = Counter(t)
    
    # Number of unique characters in t that need to be in window
    required = len(t_count)
    
    # Left and right pointers for sliding window
    left = 0
    right = 0
    
    # Number of unique characters in current window 
    # that match required frequency from t
    formed = 0
    
    # Frequency map for current window
    window_count = {}
    
    # Result: (window length, left index, right index)
    # Initialize with infinity to track minimum
    ans = float("inf"), None, None
    
    while right < len(s):
        # Add character from right side of window
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if current character's frequency matches required frequency from t
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # Try to shrink window from left while it's still valid
        while left <= right and formed == required:
            char = s[left]
            
            # Update minimum window if current is smaller
            window_length = right - left + 1
            if window_length < ans[0]:
                ans = (window_length, left, right)
            
            # Remove left character from window
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            
            # Move left pointer to shrink window
            left += 1
        
        # Expand window by moving right pointer
        right += 1
    
    # Return result
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


# ==================== TEST CASES ====================

def run_tests():
    test_cases = [
        {
            "s": "ADOBECODEBANC",
            "t": "ABC",
            "expected": "BANC",
            "description": "Standard case with multiple possible windows"
        },
        {
            "s": "a",
            "t": "a",
            "expected": "a",
            "description": "Single character match"
        },
        {
            "s": "a",
            "t": "aa",
            "expected": "",
            "description": "Not enough characters to form window"
        },
        {
            "s": "aa",
            "t": "aa",
            "expected": "aa",
            "description": "Duplicate characters required"
        },
        {
            "s": "ABCDEF",
            "t": "ACF",
            "expected": "ABCDEF",
            "description": "Entire string is minimum window"
        },
        {
            "s": "cabwefgewcwaefgcf",
            "t": "cae",
            "expected": "cwae",
            "description": "Complex case with overlapping windows"
        }
    ]
    
    print("=" * 60)
    print("Running Test Cases for Minimum Window Substring")
    print("=" * 60)
    
    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result = minWindow(test["s"], test["t"])
        status = "✅ PASS" if result == test["expected"] else "❌ FAIL"
        
        if result != test["expected"]:
            all_passed = False
        
        print(f"\nTest {i}: {test['description']}")
        print(f"  Input:    s = '{test['s']}', t = '{test['t']}'")
        print(f"  Expected: '{test['expected']}'")
        print(f"  Got:      '{result}'")
        print(f"  Status:   {status}")
    
    print("\n" + "=" * 60)
    print(f"Final Result: {'All tests passed! 🎉' if all_passed else 'Some tests failed! ❌'}")
    print("=" * 60)

run_tests()