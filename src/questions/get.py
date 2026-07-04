"""
This module provides a function to retrieve the content
of a question based on its ID and title.
"""
from pathlib import Path
import json

from src.questions.extract import extract as extract_question

def get(question_id: str, title: str) -> str:
    """
    Retrieve the content of a question based on its ID and title.
    :param question_id:
    :param title:
    :return:
    """
    file_name = f"{question_id}_{title.replace(' ', '_').lower()}"
    problems_dir = Path(__file__).resolve().parents[2] / 'content' / 'problems'
    question_dir = problems_dir / file_name

    if not question_dir.exists() or not question_dir.is_dir():
        project_root: Path = Path(__file__).resolve().parents[2]
        base: Path = project_root / 'content' / 'lists' / 'complete'
        sorted_questions: Path = base / 'sorted_questions.json'

        with open(sorted_questions, encoding='utf-8') as f:
            data: dict = json.load(f)
            question_config = data[question_id]
            if not question_config:
                raise ValueError(f"Question with id '{question_id}' "
                                 f"not found in the complete list.")
            slug = question_config['slug']
            question_info: dict = extract_question(slug)
            question_dir.mkdir(parents=True, exist_ok=True)
            question_file_path: Path = question_dir / 'question.txt'
            question_file_path.write_text(question_info['content'], encoding='utf-8')

    question_file_path:Path = question_dir / 'question.txt'
    question: str = question_file_path.read_text(encoding='utf-8')
    return question


__all__ = [
    'get',
]


def main():
    """
    Main function to test the get_question_and_answer function with a
    specific question id and title.
    :return:
    """
    question_id: str = '2'
    title: str = 'Add Two Numbers'
    question_text: str = get(question_id, title)
    print(question_text)


if __name__ == '__main__':
    main()
