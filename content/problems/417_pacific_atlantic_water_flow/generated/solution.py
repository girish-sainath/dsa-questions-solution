from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        def bfs(starts):
            """
            Perform BFS from ocean borders inward.
            Water flows backwards: from ocean to higher/equal cells.
            """
            visited = set(starts)
            queue = deque(starts)
            
            while queue:
                r, c = queue.popleft()
                
                # Check all 4 directions
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    
                    # Valid cell, not visited, and height >= current (reverse flow)
                    if (0 <= nr < m and 
                        0 <= nc < n and 
                        (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]):
                        
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return visited
        
        # Pacific Ocean borders: top row and left column
        pacific_starts = []
        for c in range(n):
            pacific_starts.append((0, c))      # Top row
        for r in range(1, m):
            pacific_starts.append((r, 0))      # Left column
        
        # Atlantic Ocean borders: bottom row and right column
        atlantic_starts = []
        for c in range(n):
            atlantic_starts.append((m - 1, c)) # Bottom row
        for r in range(m - 1):
            atlantic_starts.append((r, n - 1)) # Right column
        
        # Find cells reachable from each ocean
        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)
        
        # Find intersection: cells that can reach BOTH oceans
        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    result1 = solution.pacificAtlantic(heights1)
    print(f"Test 1 Output: {result1}")
    print(f"Expected:      [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]")
    print()
    
    # Test Case 2
    heights2 = [[1]]
    result2 = solution.pacificAtlantic(heights2)
    print(f"Test 2 Output: {result2}")
    print(f"Expected:      [[0,0]]")