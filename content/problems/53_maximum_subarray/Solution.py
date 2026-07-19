"""

"""
# pylint: disable=invalid-name, too-few-public-methods
class Solution:
    """

    """
    @staticmethod
    def maximum_subarray(nums: list[int]) -> int:
        """

        """
        max_sum: int = nums[0]
        curr_sum: int = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


def main():
    """

    """
    input_list = [
        ([[-2,1,-3,4,-1,2,1,-5,4]], 6),
        ([[1]], 1),
        ([[5,4,-1,7,8]], 23),
    ]

    solution = Solution()
    method_name = 'maximum_subarray'

    print(f'Calling method "{method_name}"')
    for input_item in input_list:
        input_values = input_item[0]
        expected_output = input_item[1]
        method_to_call = getattr(solution, method_name)
        actual_output = method_to_call(*input_values)
        print(f'{method_name}{input_values} = {actual_output} == {expected_output} -> {expected_output == actual_output}\n')


if __name__ == '__main__':
    main()
