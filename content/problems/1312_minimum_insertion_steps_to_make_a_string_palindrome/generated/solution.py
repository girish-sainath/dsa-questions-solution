from typing import List

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        """
        Count the number of artifacts that can be fully extracted.
        
        Args:
            n: Size of the n x n grid
            artifacts: List of [r1, c1, r2, c2] representing artifact boundaries
            dig: List of [r, c] representing excavated cells
            
        Returns:
            Number of artifacts that can be fully extracted
        """
        # Convert dig positions to a set for O(1) lookup
        excavated = set()
        for r, c in dig:
            excavated.add((r, c))
        
        count = 0
        
        # Check each artifact
        for r1, c1, r2, c2 in artifacts:
            can_extract = True
            
            # Iterate through all cells covered by this artifact
            for row in range(r1, r2 + 1):
                for col in range(c1, c2 + 1):
                    if (row, col) not in excavated:
                        can_extract = False
                        break
                if not can_extract:
                    break
            
            if can_extract:
                count += 1
        
        return count


# Test cases
def main():
    solution = Solution()
    
    # Example 1
    n = 2
    artifacts = [[0,0,0,0],[0,1,1,1]]
    dig = [[0,0],[0,1]]
    result = solution.digArtifacts(n, artifacts, dig)
    print(f"Example 1: {result}")  # Expected: 1
    
    # Example 2
    n = 2
    artifacts = [[0,0,0,0],[0,1,1,1]]
    dig = [[0,0],[0,1],[1,1]]
    result = solution.digArtifacts(n, artifacts, dig)
    print(f"Example 2: {result}")  # Expected: 2
    
    # Additional test: No artifacts extractable
    n = 3
    artifacts = [[0,0,1,1]]
    dig = [[0,0],[0,1]]
    result = solution.digArtifacts(n, artifacts, dig)
    print(f"Additional Test 1 (partial dig): {result}")  # Expected: 0
    
    # Additional test: All artifacts extractable
    n = 3
    artifacts = [[0,0,1,1]]
    dig = [[0,0],[0,1],[1,0],[1,1]]
    result = solution.digArtifacts(n, artifacts, dig)
    print(f"Additional Test 2 (full dig): {result}")  # Expected: 1


if __name__ == "__main__":
    main()