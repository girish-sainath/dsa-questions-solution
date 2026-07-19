from collections import Counter
from typing import List


def minInterval(tasks: List[str], n: int) -> int:
    """
    Calculate minimum CPU intervals required to complete all tasks.
    
    Args:
        tasks: List of task labels
        n: Minimum gap required between same tasks
    
    Returns:
        Minimum number of CPU intervals
    """
    # Step 1: Count frequency of each task
    task_counts = Counter(tasks)
    
    # Step 2: Find the maximum frequency
    max_freq = max(task_counts.values())
    
    # Step 3: Count how many tasks have the maximum frequency
    count_max_freq = sum(1 for count in task_counts.values() if count == max_freq)
    
    # Step 4: Calculate minimum intervals using the formula
    # (max_freq - 1) creates the number of "frames" needed
    # Each frame needs (n + 1) slots
    # Add count_max_freq for the last partial frame
    calculated = (max_freq - 1) * (n + 1) + count_max_freq
    
    # The answer is at least the total number of tasks
    return max(len(tasks), calculated)


# Test cases
if __name__ == "__main__":
    test_cases = [
        {
            "tasks": ["A", "A", "A", "B", "B", "B"],
            "n": 2,
            "expected": 8,
            "explanation": "A -> B -> idle -> A -> B -> idle -> A -> B"
        },
        {
            "tasks": ["A", "C", "A", "B", "D", "B"],
            "n": 1,
            "expected": 6,
            "explanation": "A -> B -> C -> D -> A -> B"
        },
        {
            "tasks": ["A", "A", "A", "B", "B", "B"],
            "n": 3,
            "expected": 10,
            "explanation": "A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B"
        },
        {
            "tasks": ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
            "n": 2,
            "expected": 16,
            "explanation": "Many tasks, A dominates"
        },
        {
            "tasks": ["A"],
            "n": 0,
            "expected": 1,
            "explanation": "Single task"
        }
    ]
    
    print("=" * 65)
    print(f"{'Test':<6} {'Tasks':<35} {'n':<4} {'Expected':<10} {'Got':<8} {'Pass'}")
    print("=" * 65)
    
    for i, tc in enumerate(test_cases, 1):
        result = minInterval(tc["tasks"], tc["n"])
        passed = "✓" if result == tc["expected"] else "✗"
        tasks_str = str(tc["tasks"])[:33]
        print(f"{i:<6} {tasks_str:<35} {tc['n']:<4} {tc['expected']:<10} {result:<8} {passed}")
        print(f"       Explanation: {tc['explanation']}")
        print("-" * 65)