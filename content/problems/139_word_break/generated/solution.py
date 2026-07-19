from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Dynamic Programming approach to solve Word Break problem.
        
        Args:
            s: Input string to be segmented
            wordDict: List of valid dictionary words
            
        Returns:
            True if s can be segmented into dictionary words, False otherwise
            
        Time Complexity: O(n^2) where n is length of string s
        Space Complexity: O(n) for the DP array
        """
        word_set = set(wordDict)  # Convert to set for O(1) lookup
        n = len(s)
        
        # dp[i] = True means s[0:i] can be segmented using dictionary words
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always valid
        
        for i in range(1, n + 1):
            for j in range(i):
                # Check if s[0:j] is valid AND s[j:i] is in dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further once dp[i] is True
        
        return dp[n]


# Test cases
def run_tests():
    solution = Solution()
    
    # Test Case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    result1 = solution.wordBreak(s1, wordDict1)
    print(f"Test 1: s = '{s1}', wordDict = {wordDict1}")
    print(f"Output: {result1}")
    print(f"Expected: True\n")
    
    # Test Case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    result2 = solution.wordBreak(s2, wordDict2)
    print(f"Test 2: s = '{s2}', wordDict = {wordDict2}")
    print(f"Output: {result2}")
    print(f"Expected: True\n")
    
    # Test Case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    result3 = solution.wordBreak(s3, wordDict3)
    print(f"Test 3: s = '{s3}', wordDict = {wordDict3}")
    print(f"Output: {result3}")
    print(f"Expected: False\n")


if __name__ == "__main__":
    run_tests()