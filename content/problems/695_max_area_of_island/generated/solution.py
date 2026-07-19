from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        
        def dfs(row: int, col: int) -> int:
            """
            Perform DFS from (row, col) and return the area of the island.
            Mark visited cells by setting them to 0.
            """
            # Base case: out of bounds or water cell
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            
            # Mark current cell as visited by setting it to 0
            grid[row][col] = 0
            
            # Explore all 4 directions and accumulate area
            area = 1  # Count current cell
            area += dfs(row + 1, col)  # Down
            area += dfs(row - 1, col)  # Up
            area += dfs(row, col + 1)  # Right
            area += dfs(row, col - 1)  # Left
            
            return area
        
        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Found an unvisited island, calculate its area
                    island_area = dfs(r, c)
                    max_area = max(max_area, island_area)
        
        return max_area


# ==================== TEST CASES ====================

def test_solution():
    solution = Solution()
    
    # Test Case 1
    grid1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    result1 = solution.maxAreaOfIsland(grid1)
    print(f"Test 1 - Expected: 6, Got: {result1} {'✓' if result1 == 6 else '✗'}")
    
    # Test Case 2
    grid2 = [[0,0,0,0,0,0,0,0]]
    result2 = solution.maxAreaOfIsland(grid2)
    print(f"Test 2 - Expected: 0, Got: {result2} {'✓' if result2 == 0 else '✗'}")
    
    # Test Case 3: Single cell island
    grid3 = [[1]]
    result3 = solution.maxAreaOfIsland(grid3)
    print(f"Test 3 - Expected: 1, Got: {result3} {'✓' if result3 == 1 else '✗'}")
    
    # Test Case 4: Entire grid is one island
    grid4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    result4 = solution.maxAreaOfIsland(grid4)
    print(f"Test 4 - Expected: 9, Got: {result4} {'✓' if result4 == 9 else '✗'}")
    
    # Test Case 5: Multiple islands, pick the largest
    grid5 = [
        [1, 0, 1],
        [0, 0, 1],
        [1, 0, 1]
    ]
    result5 = solution.maxAreaOfIsland(grid5)
    print(f"Test 5 - Expected: 2, Got: {result5} {'✓' if result5 == 2 else '✗'}")

test_solution()