"""

"""
# pylint: disable=invalid-name, too-few-public-methods
class Solution:
    """

    """
    @staticmethod
    def pacific_atlantic_water_flow():
        """

        """


def main():
    """

    """
    input_list = []

    solution = Solution()
    method_name = 'pacific_atlantic_water_flow'

    print(f'Calling method "{method_name}"')
    for input_item in input_list:
        input_values = input_item[0]
        expected_output = input_item[1]
        method_to_call = getattr(solution, method_name)
        actual_output = method_to_call(*input_values)
        print(f'{method_name}{input_values} = {actual_output} == {expected_output} -> {expected_output == actual_output}\n')


if __name__ == '__main__':
    main()
