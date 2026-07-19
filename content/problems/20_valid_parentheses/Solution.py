"""

"""
# pylint: disable=invalid-name, too-few-public-methods
class Solution:
    """

    """
    @staticmethod
    def valid_parentheses(input_str: str) -> bool:
        """

        """
        stack: list[str] = []
        bracket_map: dict[str, str] = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in input_str:
            if char in bracket_map:
                top = stack.pop() if stack else '#'

                if top != bracket_map[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


def main():
    """

    """
    input_list = [
        (['()'], True),
        (['()[]{}'], True),
        (['(]'], False),
        (['([)]'], False),
        (['{[]}'], True),
        ([''], True),
        (['(((((((((())))))))))'], True),
        (['(((((((((()))))))))))'], False),
        (['{[()]}'], True),
        (['{[(])}'], False),
    ]

    solution = Solution()
    method_name = 'valid_parentheses'

    print(f'Calling method "{method_name}"')
    for input_item in input_list:
        input_values = input_item[0]
        expected_output = input_item[1]
        method_to_call = getattr(solution, method_name)
        actual_output = method_to_call(*input_values)
        print(f'{method_name}{input_values} = {actual_output} == {expected_output} -> {expected_output == actual_output}\n')


if __name__ == '__main__':
    main()
