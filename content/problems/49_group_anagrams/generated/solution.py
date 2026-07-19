from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams together from a list of strings.
    
    Args:
        strs: List of strings to group
        
    Returns:
        List of groups where each group contains anagrams
    """
    # Dictionary to store groups: sorted_string -> list of anagrams
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Sort the string to create a unique key for all its anagrams
        sorted_key = tuple(sorted(s))  # tuple is hashable (can be used as dict key)
        anagram_groups[sorted_key].append(s)
    
    # Return all groups as a list of lists
    return list(anagram_groups.values())


# ==================== Test Cases ====================
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = groupAnagrams(strs1)
    print(f"Input:  {strs1}")
    print(f"Output: {result1}")
    print()

    # Test Case 2
    strs2 = [""]
    result2 = groupAnagrams(strs2)
    print(f"Input:  {strs2}")
    print(f"Output: {result2}")
    print()

    # Test Case 3
    strs3 = ["a"]
    result3 = groupAnagrams(strs3)
    print(f"Input:  {strs3}")
    print(f"Output: {result3}")
    print()

    # Additional Test Case - all same anagrams
    strs4 = ["abc", "bca", "cab", "xyz", "zyx"]
    result4 = groupAnagrams(strs4)
    print(f"Input:  {strs4}")
    print(f"Output: {result4}")