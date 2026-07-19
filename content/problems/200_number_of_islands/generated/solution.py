from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        
        def dfs(r: int, c: int) -> None:
            """
            Depth-First Search to mark all connected land cells as visited.
            We mark visited cells by changing '1' to '0' to avoid revisiting.
            """
            # Base case: out of bounds or water/visited cell
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Mark current cell as visited
            grid[r][c] = '0'
            
            # Explore all 4 adjacent directions (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1  # Found a new island
                    dfs(r, c)          # Sink the entire island
        
        return island_count


# ------------------- Test Cases -------------------
def run_tests():
    solution = Solution()
    
    # Test Case 1: Single large island
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    result1 = solution.numIslands(grid1)
    print(f"Test 1 - Expected: 1, Got: {result1} {'✓' if result1 == 1 else '✗'}")
    
    # Test Case 2: Multiple islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    result2 = solution.numIslands(grid2)
    print(f"Test 2 - Expected: 3, Got: {result2} {'✓' if result2 == 3 else '✗'}")
    
    # Test Case 3: All water
    grid3 = [
        ["0","0","0"],
        ["0","0","0"]
    ]
    result3 = solution.numIslands(grid3)
    print(f"Test 3 - Expected: 0, Got: {result3} {'✓' if result3 == 0 else '✗'}")
    
    # Test Case 4: All land (one island)
    grid4 = [
        ["1","1","1"],
        ["1","1","1"]
    ]
    result4 = solution.numIslands(grid4)
    print(f"Test 4 - Expected: 1, Got: {result4} {'✓' if result4 == 1 else '✗'}")
    
    # Test Case 5: Each cell is a separate island
    grid5 = [
        ["1","0","1"],
        ["0","1","0"],
        ["1","0","1"]
    ]
    result5 = solution.numIslands(grid5)
    print(f"Test 5 - Expected: 5, Got: {result5} {'✓' if result5 == 5 else '✗'}")

run_tests()