"""

"""
from collections import Counter
# pylint: disable=invalid-name, too-few-public-methods
class Solution:
    """

    """
    @staticmethod
    def minimum_window_substring(s: str, t: str) -> str:
        """

        """
        t_count = Counter(t)

        required = len(t_count)

        left = 0
        right = 0
        formed = 0

        window_count = {}

        ans = float('inf'), None, None

        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char , 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                window_length = right - left + 1
                if window_length < ans[0]:
                    ans = (window_length, left, right)

                window_count[char] -= 1

                if char in t_count and window_count[char] < t_count[char]:
                    formed -=1

                left += 1

            right += 1

        return '' if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]



def main():
    """

    """
    input_list = [
        (['ADOBECODEBANC', 'ABC'], 'BANC'),
        (['a', 'a'], 'a'),
        (['a', 'aa'], ''),
        (['aa', 'aa'], 'aa'),
        (['ABCDEF', 'ACF'], 'ABCDEF'),
        (['cabwefgewcwaefgcf', 'cae'], 'cwae')
    ]

    solution = Solution()
    method_name = 'minimum_window_substring'

    print(f'Calling method "{method_name}"')
    for input_item in input_list:
        input_values = input_item[0]
        expected_output = input_item[1]
        method_to_call = getattr(solution, method_name)
        actual_output = method_to_call(*input_values)
        print(f'{method_name}{input_values} = {actual_output} == {expected_output} -> {expected_output == actual_output}\n')


if __name__ == '__main__':
    main()
