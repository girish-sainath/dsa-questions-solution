from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Detect cycle in directed graph using DFS.
        
        Args:
            numCourses: Total number of courses (nodes)
            prerequisites: List of [course, prerequisite] pairs (directed edges)
            
        Returns:
            True if all courses can be finished (no cycle), False otherwise
        """
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def has_cycle(node: int) -> bool:
            """Returns True if a cycle is detected starting from node."""
            if state[node] == 1:  # Currently being visited -> cycle detected
                return True
            if state[node] == 2:  # Already fully visited -> no cycle from here
                return False
            
            # Mark node as currently being visited
            state[node] = 1
            
            # Visit all neighbors
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            
            # Mark node as fully visited
            state[node] = 2
            return False
        
        # Check each node for cycles (handles disconnected graphs)
        for course in range(numCourses):
            if has_cycle(course):
                return False
        
        return True


# ==================== Testing ====================
def test_solution():
    solution = Solution()
    
    # Test Case 1: Simple valid case
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    result1 = solution.canFinish(numCourses1, prerequisites1)
    print(f"Test 1 - Input: numCourses={numCourses1}, prerequisites={prerequisites1}")
    print(f"         Expected: True, Got: {result1}")
    print(f"         {'✓ PASS' if result1 == True else '✗ FAIL'}\n")
    
    # Test Case 2: Circular dependency
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    result2 = solution.canFinish(numCourses2, prerequisites2)
    print(f"Test 2 - Input: numCourses={numCourses2}, prerequisites={prerequisites2}")
    print(f"         Expected: False, Got: {result2}")
    print(f"         {'✓ PASS' if result2 == False else '✗ FAIL'}\n")
    
    # Test Case 3: No prerequisites
    numCourses3 = 3
    prerequisites3 = []
    result3 = solution.canFinish(numCourses3, prerequisites3)
    print(f"Test 3 - Input: numCourses={numCourses3}, prerequisites={prerequisites3}")
    print(f"         Expected: True, Got: {result3}")
    print(f"         {'✓ PASS' if result3 == True else '✗ FAIL'}\n")
    
    # Test Case 4: Longer cycle
    numCourses4 = 4
    prerequisites4 = [[1, 0], [2, 1], [3, 2], [0, 3]]
    result4 = solution.canFinish(numCourses4, prerequisites4)
    print(f"Test 4 - Input: numCourses={numCourses4}, prerequisites={prerequisites4}")
    print(f"         Expected: False, Got: {result4}")
    print(f"         {'✓ PASS' if result4 == False else '✗ FAIL'}\n")
    
    # Test Case 5: Linear chain (no cycle)
    numCourses5 = 4
    prerequisites5 = [[1, 0], [2, 1], [3, 2]]
    result5 = solution.canFinish(numCourses5, prerequisites5)
    print(f"Test 5 - Input: numCourses={numCourses5}, prerequisites={prerequisites5}")
    print(f"         Expected: True, Got: {result5}")
    print(f"         {'✓ PASS' if result5 == True else '✗ FAIL'}\n")


if __name__ == "__main__":
    test_solution()