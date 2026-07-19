"""

"""
# pylint: disable=invalid-name, too-few-public-methods
class Solution:
    """

    """
    @staticmethod
    def merge_intervals(intervals: list[list[str]]) -> list[list[str]]:
        """

        """
        intervals.sort(key=lambda x: x[0])
        merged: list[list[str]] = []

        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


def main():
    """

    """
    input_list = [
        ([[[1,3],[2,6],[8,10],[15,18]]], [[1,6],[8,10],[15,18]]),
        ([[[1,4],[4,5]]], [[1,5]]),
        ([[[4,7],[1,4]]], [[1,7]]),
    ]

    solution = Solution()
    method_name = 'merge_intervals'

    print(f'Calling method "{method_name}"')
    for input_item in input_list:
        input_values = input_item[0]
        expected_output = input_item[1]
        method_to_call = getattr(solution, method_name)
        actual_output = method_to_call(*input_values)
        print(f'{method_name}{input_values} = {actual_output} == {expected_output} -> {expected_output == actual_output}\n')


if __name__ == '__main__':
    main()
