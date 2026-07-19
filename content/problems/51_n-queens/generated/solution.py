from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        # Track occupied columns and diagonals
        cols = set()
        diag1 = set()  # top-left to bottom-right (row - col)
        diag2 = set()  # top-right to bottom-left (row + col)
        
        # queens[i] = column position of queen in row i
        queens = []
        
        def backtrack(row: int):
            # Base case: all queens placed successfully
            if row == n:
                # Build board from queens placement
                board = []
                for col in queens:
                    board.append('.' * col + 'Q' + '.' * (n - col - 1))
                results.append(board)
                return
            
            # Try placing queen in each column of current row
            for col in range(n):
                # Skip if column or diagonal is already occupied
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                queens.append(col)
                
                # Recurse to next row
                backtrack(row + 1)
                
                # Remove queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                queens.pop()
        
        backtrack(0)
        return results


# ------------------- Test Cases -------------------
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: n = 4
    n = 4
    result = solution.solveNQueens(n)
    print(f"n = {n}: {len(result)} solutions found")
    for board in result:
        for row in board:
            print(f"  {row}")
        print()
    
    # Test Case 2: n = 1
    n = 1
    result = solution.solveNQueens(n)
    print(f"n = {n}: {len(result)} solutions found")
    for board in result:
        for row in board:
            print(f"  {row}")
        print()
    
    # Test Case 3: n = 8 (classic 8-queens problem)
    n = 8
    result = solution.solveNQueens(n)
    print(f"n = {n}: {len(result)} solutions found")