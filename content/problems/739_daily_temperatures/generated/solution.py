from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    """
    Find number of days to wait for a warmer temperature.
    
    Args:
        temperatures: List of daily temperatures
        
    Returns:
        List where answer[i] = days to wait for warmer temp after day i
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Monotonic decreasing stack storing indices
    
    for i in range(n):
        # While current temp is warmer than temp at stack's top index
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index  # Days waited
        
        stack.append(i)
    
    # Remaining indices in stack have no warmer future day (answer stays 0)
    return answer


# ─── Test Cases ───────────────────────────────────────────────────────────────

def run_tests():
    test_cases = [
        {
            "input": [73, 74, 75, 71, 69, 72, 76, 73],
            "expected": [1, 1, 4, 2, 1, 1, 0, 0]
        },
        {
            "input": [30, 40, 50, 60],
            "expected": [1, 1, 1, 0]
        },
        {
            "input": [30, 60, 90],
            "expected": [1, 1, 0]
        },
        {
            "input": [90, 80, 70, 60],  # Strictly decreasing
            "expected": [0, 0, 0, 0]
        },
        {
            "input": [60, 70, 80, 90],  # Strictly increasing
            "expected": [1, 1, 1, 0]
        },
        {
            "input": [50],              # Single element
            "expected": [0]
        }
    ]
    
    print("=" * 55)
    print(f"{'Test':<6} {'Status':<10} {'Input':<25} {'Output'}")
    print("=" * 55)
    
    for idx, tc in enumerate(test_cases, 1):
        result = dailyTemperatures(tc["input"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        print(f"{idx:<6} {status:<10} {str(tc['input']):<25} {result}")
    
    print("=" * 55)


if __name__ == "__main__":
    run_tests()