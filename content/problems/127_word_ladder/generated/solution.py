from collections import deque
from typing import List


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Find the length of shortest transformation sequence from beginWord to endWord.
    
    Args:
        beginWord: Starting word
        endWord: Target word
        wordList: List of valid intermediate words
        
    Returns:
        Length of shortest transformation sequence, or 0 if none exists
    """
    # Convert wordList to a set for O(1) lookup
    word_set = set(wordList)
    
    # If endWord is not in wordList, no valid transformation exists
    if endWord not in word_set:
        return 0
    
    # BFS queue: stores (current_word, current_length)
    queue = deque([(beginWord, 1)])
    
    # Track visited words to avoid cycles
    visited = {beginWord}
    
    while queue:
        current_word, length = queue.popleft()
        
        # Try changing each character position
        for i in range(len(current_word)):
            # Try all 26 possible letters
            for char in 'abcdefghijklmnopqrstuvwxyz':
                # Skip if same character
                if char == current_word[i]:
                    continue
                
                # Create new word with one character changed
                next_word = current_word[:i] + char + current_word[i+1:]
                
                # Found the endWord
                if next_word == endWord:
                    return length + 1
                
                # Add to queue if valid and not visited
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
    
    # No transformation sequence found
    return 0


# Test cases
if __name__ == "__main__":
    # Example 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result1 = ladderLength(beginWord1, endWord1, wordList1)
    print(f"Example 1: {result1}")  # Expected: 5
    
    # Example 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    result2 = ladderLength(beginWord2, endWord2, wordList2)
    print(f"Example 2: {result2}")  # Expected: 0
    
    # Additional test case
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    result3 = ladderLength(beginWord3, endWord3, wordList3)
    print(f"Example 3: {result3}")  # Expected: 2