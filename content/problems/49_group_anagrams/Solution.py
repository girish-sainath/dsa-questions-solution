"""

"""
# pylint: disable=invalid-name, too-few-public-methods
class Solution:
    """

    """

    @staticmethod
    def _group_anagrams_default_dict(strs: list[str]) -> list[list[str]]:
        """

        """
        from collections import defaultdict
        anagram_groups = defaultdict(list)

        for  s in strs:
            sorted_key = tuple(sorted(s))
            anagram_groups[sorted_key].append(s)

        return list(anagram_groups.values())


    @staticmethod
    def _group_anagrams_direct(strs: list[str]) -> list[list[str]]:
        """

        """
        anagram_groups: dict[tuple, list[str]] = {}

        for s in strs:
            sorted_key = tuple(sorted(s))
            if not sorted_key in anagram_groups:
                anagram_groups[sorted_key] = []
            anagram_groups[sorted_key].append(s)

        return list(anagram_groups.values())


    @staticmethod
    def group_anagrams(strs: list[str]) -> list[list[str]]:
        """

        """
        mode = 'default'
        if mode == 'default':
            return Solution._group_anagrams_default_dict(strs)
        else:
            return Solution._group_anagrams_direct(strs)


def main():
    """

    """
    input_list = [
        ([["eat", "tea", "tan", "ate", "nat", "bat"]], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([[""]], [[""]]),
        ([["a"]], [["a"]]),
        ([["abc", "bca", "cab", "xyz", "zyx"]], [["abc", "bca", "cab"], ["xyz", "zyx"]]),

    ]

    solution = Solution()
    method_name = 'group_anagrams'

    print(f'Calling method "{method_name}"')
    for input_item in input_list:
        input_values = input_item[0]
        expected_output = input_item[1]
        method_to_call = getattr(solution, method_name)
        actual_output = method_to_call(*input_values)
        print(f'{method_name}{input_values} = {actual_output} == {expected_output} -> {expected_output == actual_output}\n')


if __name__ == '__main__':
    main()
