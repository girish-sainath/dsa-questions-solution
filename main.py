"""
This script is the entry point for fetching a question and generating a solution for it.
"""

import json
from pathlib import Path

from src.questions.get import get as get_question
from src.solutions.generate import generate as generate_solution


def get_question_and_solution(question_id: str, title: str) -> None:
    """
    Fetch the question using the provided question_id and title,
    then generate a solution for it.
    :param question_id:
    :param title:
    :return:
    """
    print(f'Fetching question and generating solution for '
          f'question_id: {question_id} and title: {title}')
    question = get_question(question_id, title)
    print(f'Question fetched successfully for '
          f'question_id: {question_id} and title: {title}')
    generate_solution(question_id, title, question)
    print(f'Solution generated and saved successfully for '
          f'question_id: {question_id} and title: {title}')


def call_list_with_range(list_name: str, start: int, end: int) -> None:
    """
    Fetch questions from a specified list within a given range and generate solutions for them.
    Args:
        list_name: The name of the list to fetch questions from.
        start: The starting index of the questions to fetch.
        end: The ending index of the questions to fetch.
    """
    project_root: Path = Path(__file__).resolve().parent
    base: Path = project_root / 'content' / 'lists' / list_name
    questions_file: Path = base / 'formatted_questions.json'

    data = []
    with open(questions_file, encoding='utf-8') as f:
        data: list[dict] = json.load(f)

    for i in range(start, end):
        question_info = data[i]
        question_id = str(question_info['id'])
        title = question_info['title']
        get_question_and_solution(question_id=question_id, title=title)


def main() -> None:
    """
    Main function to fetch a question and generate a solution for it.
    :return:
    """

    default_list = []

    exec_option = input('Do you want to execute a single question or a list of questions? (single/list/default): ').strip().lower()
    if exec_option == 'single':
        question_id = input('Enter the question ID: ').strip()
        title = input('Enter the question title: ').strip()
        get_question_and_solution(question_id, title)
    elif exec_option == 'list':
        list_name = input('Enter the list name: ').strip()
        start = int(input('Enter the starting index (0-based): ').strip())
        end = int(input('Enter the ending index (exclusive): ').strip())
        call_list_with_range(list_name=list_name, start=start, end=end)
    elif exec_option == 'default':
        for question_info in default_list:
            question_id = str(question_info['id'])
            title = question_info['title']
            get_question_and_solution(question_id=question_id, title=title)
    else:
        print('Invalid option. Please enter "single" or "list".')


if __name__ == '__main__':
    main()
