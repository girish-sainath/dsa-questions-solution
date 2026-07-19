from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Determine the order of characters in an alien language using topological sort.
        
        Args:
            words: List of words sorted in alien language order
            
        Returns:
            String representing character order, or "" if invalid
        """
        
        # Step 1: Initialize adjacency list and in-degree count for ALL unique characters
        adj = defaultdict(set)   # adjacency list: char -> set of chars that come after it
        in_degree = {char: 0 for word in words for char in word}
        
        # Step 2: Compare adjacent words to build the graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Edge case: word1 is longer than word2 but word2 is a prefix of word1
            # e.g., ["abcd", "abc"] is INVALID in any lexicographic ordering
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            # Find the first differing character
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # word1[j] comes before word2[j] in alien language
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break  # Only the first difference gives us ordering info
        
        # Step 3: BFS Topological Sort (Kahn's Algorithm)
        # Start with all characters that have no dependencies (in_degree == 0)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            
            # Reduce in-degree for all neighbors
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check for cycle
        # If result doesn't contain all characters, a cycle exists
        if len(result) != len(in_degree):
            return ""
        
        return "".join(result)


# ============================================================
# Test Cases
# ============================================================

def run_tests():
    solution = Solution()
    
    # Test Case 1: Standard example
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    result1 = solution.alienOrder(words1)
    print(f"Test 1: {words1}")
    print(f"Output: '{result1}'")
    print(f"Expected: 'wertf' (or any valid ordering)")
    print()
    
    # Test Case 2: Simple two-word example
    words2 = ["z", "x"]
    result2 = solution.alienOrder(words2)
    print(f"Test 2: {words2}")
    print(f"Output: '{result2}'")
    print(f"Expected: 'zx'")
    print()
    
    # Test Case 3: Invalid - cycle exists
    words3 = ["z", "x", "z"]
    result3 = solution.alienOrder(words3)
    print(f"Test 3: {words3}")
    print(f"Output: '{result3}'")
    print(f"Expected: ''")
    print()
    
    # Test Case 4: Single word
    words4 = ["abc"]
    result4 = solution.alienOrder(words4)
    print(f"Test 4: {words4}")
    print(f"Output: '{result4}'")
    print(f"Expected: any permutation of 'abc'")
    print()
    
    # Test Case 5: Invalid - prefix issue
    words5 = ["abc", "ab"]
    result5 = solution.alienOrder(words5)
    print(f"Test 5: {words5}")
    print(f"Output: '{result5}'")
    print(f"Expected: ''")
    print()
    
    # Test Case 6: All same characters
    words6 = ["aa", "aab"]
    result6 = solution.alienOrder(words6)
    print(f"Test 6: {words6}")
    print(f"Output: '{result6}'")
    print(f"Expected: 'ab' or 'ba' (no ordering constraint between a and b... wait a comes before b)")
    print()

run_tests()