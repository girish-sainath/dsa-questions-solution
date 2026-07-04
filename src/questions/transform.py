"""
This script transforms the raw JSON data of a
LeetCode question list into a structured format.
"""

import json
from pathlib import Path
from typing import Callable


def _transform_blind_75(data: dict) -> list[dict]:
    """
    Transform the raw data of the Blind 75 question
    list into a structured format.
    :param data:
    :return:
    """
    return data['data']['favoriteQuestionList']['questions']


def _transform_complete(data: dict) -> list[dict]:
    """
    Transform the raw data of the complete question
    list into a structured format.
    :param data:
    :return:
    """
    return data['questions']


TRANSFORMERS: dict[str, Callable] = {
    'blind_75': _transform_blind_75,
    'complete': _transform_complete,
}


def _transform_question(q: dict) -> dict:
    """
    Transform a single question's data into a structured format.
    :param q:
    :return:
    """
    return {
        'id': q['id'],
        'title': q['title'],
        'slug': q['titleSlug'],
        'difficulty': q['difficulty'],
        'tags': [tag['name'] for tag in q['topicTags']],
    }


def _load_raw_questions(list_name: str, raw_file: Path) -> list[dict]:
    """
    Load the raw questions for the requested list from disk.
    :param list_name:
    :param raw_file:
    :return:
    """
    transformer: Callable = TRANSFORMERS[list_name]
    with open(raw_file, encoding='utf-8') as f:
        data: dict = json.load(f)
    return transformer(data)


def _build_outputs(raw_questions: list[dict]) -> tuple[dict[str, object], int]:
    """
    Build all derived question outputs from the raw question list.
    :param raw_questions:
    :return:
    """
    formatted: list[dict] = []
    by_difficulty: dict[str, list[dict]] = {}
    by_tag: dict[str, list[dict]] = {}

    for raw_question in raw_questions:
        question: dict = _transform_question(raw_question)
        question_without_tags: dict = {
            key: value for key, value in question.items() if key != 'tags'
        }
        formatted.append(question)
        by_difficulty.setdefault(question['difficulty'], []).append(question)

        for tag in question['tags']:
            key: str = tag.lower().replace(' ', '_')
            by_tag.setdefault(key, []).append(question_without_tags)

    sorted_questions: list[dict] = sorted(formatted, key=lambda question: question['id'])
    sorted_questions_dict: dict[int, dict] = {
        question['id']: question for question in sorted_questions
    }
    outputs: dict[str, object] = {
        'formatted_questions.json': formatted,
        'sorted_questions.json': sorted_questions_dict,
        'questions_by_difficulty.json': by_difficulty,
        'questions_by_tag.json': by_tag,
    }
    return outputs, len(formatted)


def _write_outputs(base: Path, outputs: dict[str, object]) -> None:
    """
    Write transformed outputs to disk.
    :param base:
    :param outputs:
    :return:
    """
    for filename, payload in outputs.items():
        with open(base / filename, 'w', encoding='utf-8') as f:
            json.dump(payload, f, indent=4)


def transform(list_name: str) -> None:
    """
    Transform the raw JSON data of a LeetCode question list
    into a structured format and save it to files.
    :param list_name:
    :return:
    """
    if list_name not in TRANSFORMERS:
        raise ValueError(f"Unknown list '{list_name}'. Available: {list(TRANSFORMERS)}")

    project_root: Path = Path(__file__).resolve().parents[2]
    base: Path = project_root / 'content' / 'lists' / list_name
    raw_file: Path = base / 'raw_file.json'

    raw_questions: list[dict] = _load_raw_questions(list_name, raw_file)
    outputs, question_count = _build_outputs(raw_questions)
    _write_outputs(base, outputs)

    print(f"Extracted {question_count} questions from '{list_name}'")


def main():
    """
    Main function to transform the raw JSON data of the complete
    question list into a structured format.
    :return:
    """
    name = 'complete'
    transform(name)


if __name__ == '__main__':
    main()
