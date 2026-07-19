def isValid(s: str) -> bool:
    """
    Determines if the input string has valid parentheses.
    
    Args:
        s: String containing only '(', ')', '{', '}', '[', ']'
    
    Returns:
        True if valid, False otherwise
    
    Time Complexity: O(n) - single pass through string
    Space Complexity: O(n) - stack can hold at most n/2 elements
    """
    # Stack to store opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        if char in bracket_map:
            # It's a closing bracket
            # Pop from stack if not empty, otherwise use dummy value
            top = stack.pop() if stack else '#'
            
            # Check if the popped bracket matches the expected opening bracket
            if bracket_map[char] != top:
                return False
        else:
            # It's an opening bracket, push onto stack
            stack.append(char)
    
    # Valid only if stack is empty (all brackets were matched)
    return len(stack) == 0


# ============================================================
# Test Cases
# ============================================================
def run_tests():
    test_cases = [
        {"input": "()",      "expected": True,  "description": "Simple valid pair"},
        {"input": "()[]{}",  "expected": True,  "description": "Multiple valid pairs"},
        {"input": "(]",      "expected": False, "description": "Mismatched brackets"},
        {"input": "([])",    "expected": True,  "description": "Nested valid brackets"},
        {"input": "([)]",    "expected": False, "description": "Incorrectly ordered brackets"},
        {"input": "{[]}",    "expected": True,  "description": "Nested curly and square"},
        {"input": "(",       "expected": False, "description": "Unclosed opening bracket"},
        {"input": ")",       "expected": False, "description": "Unmatched closing bracket"},
        {"input": "",        "expected": True,  "description": "Empty string"},
        {"input": "{[()]}",  "expected": True,  "description": "Deeply nested brackets"},
    ]
    
    print("=" * 60)
    print(f"{'Test Case':<20} {'Expected':<10} {'Got':<10} {'Status'}")
    print("=" * 60)
    
    all_passed = True
    for i, test in enumerate(test_cases, 1):
        result = isValid(test["input"])
        status = "✅ PASS" if result == test["expected"] else "❌ FAIL"
        if result != test["expected"]:
            all_passed = False
        
        print(f"Test {i}: {test['input']:<15} {str(test['expected']):<10} {str(result):<10} {status}")
        print(f"         → {test['description']}")
    
    print("=" * 60)
    print(f"Overall: {'✅ All tests passed!' if all_passed else '❌ Some tests failed!'}")

run_tests()