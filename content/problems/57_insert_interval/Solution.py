"""

"""
# pylint: disable=invalid-name, too-few-public-methods
class Solution:
    """

    """
    @staticmethod
    def insert_interval(intervals: list[list[str]], new_interval: list[str]) -> list[list[str]]:
        """

        """
        result = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1

        result.append(new_interval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result


def main():
    """

    """
    input_list = [
        ([[[1,3],[6,9]], [2,5]], [[1,5],[6,9]]),
        ([[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]], [[1,2],[3,10],[12,16]])
    ]

    solution = Solution()
    method_name = 'insert_interval'

    print(f'Calling method "{method_name}"')
    for input_item in input_list:
        input_values = input_item[0]
        expected_output = input_item[1]
        method_to_call = getattr(solution, method_name)
        actual_output = method_to_call(*input_values)
        print(f'{method_name}{input_values} = {actual_output} == {expected_output} -> {expected_output == actual_output}\n')


if __name__ == '__main__':
    main()
