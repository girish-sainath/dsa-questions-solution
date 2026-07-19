class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Count palindromic substrings using expand around center technique.
        
        Time Complexity: O(n²) - for each center, we expand at most O(n) times
        Space Complexity: O(1) - only using constant extra space
        """
        count = 0
        n = len(s)
        
        def expand_around_center(left: int, right: int) -> int:
            """
            Expand from center and count palindromes.
            left and right are the initial center positions.
            For odd length: left == right
            For even length: right = left + 1
            """
            palindrome_count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                palindrome_count += 1
                left -= 1
                right += 1
            return palindrome_count
        
        for i in range(n):
            # Count odd-length palindromes centered at index i
            count += expand_around_center(i, i)
            
            # Count even-length palindromes centered between i and i+1
            count += expand_around_center(i, i + 1)
        
        return count


# ==================== Testing ====================
def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "input": "abc",
            "expected": 3,
            "explanation": "Three palindromic strings: 'a', 'b', 'c'"
        },
        {
            "input": "aaa",
            "expected": 6,
            "explanation": "Six palindromic strings: 'a', 'a', 'a', 'aa', 'aa', 'aaa'"
        },
        {
            "input": "a",
            "expected": 1,
            "explanation": "Single character: 'a'"
        },
        {
            "input": "aa",
            "expected": 3,
            "explanation": "Three palindromic strings: 'a', 'a', 'aa'"
        },
        {
            "input": "racecar",
            "expected": 10,
            "explanation": "'r','a','c','e','c','a','r','aca','cec','racecar' + 'aceca' = 10"
        }
    ]
    
    print("=" * 60)
    print("Testing Palindromic Substrings Solution")
    print("=" * 60)
    
    for i, test in enumerate(test_cases, 1):
        s = test["input"]
        expected = test["expected"]
        result = solution.countSubstrings(s)
        status = "✅ PASSED" if result == expected else "❌ FAILED"
        
        print(f"\nTest {i}: {status}")
        print(f"  Input:       s = '{s}'")
        print(f"  Expected:    {expected}")
        print(f"  Got:         {result}")
        print(f"  Explanation: {test['explanation']}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_tests()