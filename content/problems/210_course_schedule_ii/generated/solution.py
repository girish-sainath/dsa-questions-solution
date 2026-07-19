from collections import deque
from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Find the order to complete all courses using topological sort (Kahn's Algorithm).
    
    Args:
        numCourses: Total number of courses (labeled 0 to numCourses-1)
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        List of courses in valid completion order, or empty list if impossible
    """
    # Step 1: Build adjacency list and in-degree array
    # adj[i] contains list of courses that depend on course i
    adj = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        adj[prereq].append(course)  # prereq → course
        in_degree[course] += 1      # course needs one more prerequisite
    
    # Step 2: Initialize queue with all courses having no prerequisites
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)
    
    # Step 3: Process courses in topological order
    order = []
    
    while queue:
        # Take a course with no remaining prerequisites
        course = queue.popleft()
        order.append(course)
        
        # Reduce in-degree for all courses that depend on this course
        for next_course in adj[course]:
            in_degree[next_course] -= 1
            
            # If all prerequisites are met, add to queue
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    # Step 4: Check if all courses were processed (no cycle exists)
    return order if len(order) == numCourses else []


# ==================== Test Cases ====================

def run_tests():
    test_cases = [
        {
            "numCourses": 2,
            "prerequisites": [[1, 0]],
            "expected_length": 2,
            "description": "Simple 2 course dependency"
        },
        {
            "numCourses": 4,
            "prerequisites": [[1, 0], [2, 0], [3, 1], [3, 2]],
            "expected_length": 4,
            "description": "4 courses with multiple dependencies"
        },
        {
            "numCourses": 1,
            "prerequisites": [],
            "expected_length": 1,
            "description": "Single course, no prerequisites"
        },
        {
            "numCourses": 2,
            "prerequisites": [[1, 0], [0, 1]],
            "expected_length": 0,
            "description": "Circular dependency (impossible)"
        },
        {
            "numCourses": 3,
            "prerequisites": [[1, 0], [2, 1]],
            "expected_length": 3,
            "description": "Linear chain of prerequisites"
        }
    ]
    
    def is_valid_order(order, numCourses, prerequisites):
        """Validate that the order is a valid topological sort."""
        if not order:
            return True
        
        # Map each course to its position in the order
        position = {course: i for i, course in enumerate(order)}
        
        # Check that for every prerequisite [course, prereq],
        # prereq appears before course in the order
        for course, prereq in prerequisites:
            if position[prereq] >= position[course]:
                return False
        return True
    
    print("=" * 60)
    print("Running Test Cases for Course Schedule II")
    print("=" * 60)
    
    for i, tc in enumerate(test_cases):
        result = findOrder(tc["numCourses"], tc["prerequisites"])
        
        # Verify result length matches expected
        length_correct = len(result) == tc["expected_length"]
        
        # Verify ordering is valid (only for non-empty results)
        order_valid = True
        if result:
            order_valid = is_valid_order(result, tc["numCourses"], tc["prerequisites"])
        
        status = "✅ PASS" if (length_correct and order_valid) else "❌ FAIL"
        
        print(f"\nTest {i + 1}: {tc['description']}")
        print(f"  Input:    numCourses={tc['numCourses']}, prerequisites={tc['prerequisites']}")
        print(f"  Output:   {result}")
        print(f"  Expected: {tc['expected_length']} courses in valid order")
        print(f"  Status:   {status}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_tests()