"""
This script sorts the questions in the 'content/lists/complete_unsorted' directory by their 'id'
and saves the sorted questions to 'content/lists/complete/raw_file.json'.
"""
import json
from pathlib import Path


def sort():
    """
    Sorts the questions in the 'content/lists/complete_unsorted' directory by their 'id'
    and saves the sorted questions to 'content/lists/complete/raw_file.json'.
    :return:
    """
    project_root = Path(__file__).resolve().parents[2]
    complete_dir = project_root / 'content' / 'lists' / 'complete_unsorted'
    output_dir = project_root / 'content' / 'lists' / 'complete'
    output_dir.mkdir(parents=True, exist_ok=True)

    all_questions = []

    for file_path in sorted(complete_dir.glob('*.json')):
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        questions = data['data']['problemsetQuestionListV2']['questions']
        all_questions.extend(questions)

    all_questions.sort(key=lambda q: q['id'])

    output_file = output_dir / 'raw_file.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({'questions': all_questions}, f, indent=4)


def main():
    """
    Main function to sort the questions and save them to a JSON file.
    :return:
    """
    sort()
    print("Sorted questions and saved to 'content/lists/complete/raw_file.json'")


if __name__ == '__main__':
    main()
