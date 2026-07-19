from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Find if a word exists in the board using DFS with backtracking.
        
        Args:
            board: m x n grid of characters
            word: target word to search for
            
        Returns:
            True if word exists in grid, False otherwise
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(row: int, col: int, index: int) -> bool:
            """
            DFS helper function to explore paths.
            
            Args:
                row: current row position
                col: current column position
                index: current character index in word
                
            Returns:
                True if word can be completed from current position
            """
            # Base case: all characters matched successfully
            if index == len(word):
                return True
            
            # Boundary and character mismatch checks
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                board[row][col] != word[index]):
                return False
            
            # Mark cell as visited by temporarily modifying it
            temp = board[row][col]
            board[row][col] = '#'  # visited marker
            
            # Explore all 4 directions: up, down, left, right
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            found = any(
                dfs(row + dr, col + dc, index + 1)
                for dr, dc in directions
            )
            
            # Backtrack: restore the cell's original value
            board[row][col] = temp
            
            return found
        
        # Try starting DFS from every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False


# ============================================================
# Test Cases
# ============================================================
def run_tests():
    solution = Solution()
    
    test_cases = [
        {
            "board": [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ],
            "word": "ABCCED",
            "expected": True,
            "description": "Example 1 - Word exists going right then down"
        },
        {
            "board": [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ],
            "word": "SEE",
            "expected": True,
            "description": "Example 2 - Word exists in bottom-right area"
        },
        {
            "board": [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ],
            "word": "ABCB",
            "expected": False,
            "description": "Example 3 - Cannot reuse same cell"
        },
        {
            "board": [["A"]],
            "word": "A",
            "expected": True,
            "description": "Single cell match"
        },
        {
            "board": [["A"]],
            "word": "B",
            "expected": False,
            "description": "Single cell no match"
        },
        {
            "board": [
                ["A","B"],
                ["C","D"]
            ],
            "word": "ABDC",
            "expected": True,
            "description": "Snaking path through 2x2 grid"
        }
    ]
    
    print("=" * 60)
    print("Word Search - Test Results")
    print("=" * 60)
    
    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result = solution.exist(test["board"], test["word"])
        status = "✅ PASS" if result == test["expected"] else "❌ FAIL"
        
        if result != test["expected"]:
            all_passed = False
        
        print(f"\nTest {i}: {test['description']}")
        print(f"  Word: '{test['word']}'")
        print(f"  Expected: {test['expected']} | Got: {result} | {status}")
    
    print("\n" + "=" * 60)
    print(f"Overall: {'✅ All tests passed!' if all_passed else '❌ Some tests failed!'}")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()