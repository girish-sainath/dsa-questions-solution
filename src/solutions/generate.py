"""
This module provides functionality to generate solutions for
data structures and algorithms questions using a language model.
"""
import os
from pathlib import Path
import re
from dotenv import load_dotenv

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_litellm import ChatLiteLLM
from langchain.chat_models import init_chat_model

from src.questions.get import get as get_question


load_dotenv()


def _extract_code_from_response(response_content: str, language: str = 'python') -> str:
    """
    Extracts code blocks from the response content based on the specified language.
    :param response_content:
    :param language:
    :return:
    """
    if isinstance(response_content, list):
        content = '\n'.join(str(item) for item in response_content)
    elif isinstance(response_content, str):
        content = response_content
    else:
        content = str(response_content)

    fenced_blocks = []
    for match in re.finditer(r'```(?P<lang>[^\n`]*)\n(?P<code>.*?)```', content, re.DOTALL):
        raw_lang = match.group('lang').strip().lower()
        lang = raw_lang.split()[0] if raw_lang else ''
        code = match.group('code').strip()
        if code:
            fenced_blocks.append((lang, code))

    if not fenced_blocks:
        return content.strip()

    if language:
        requested = language.strip().lower()
        language_aliases = {
            'python': {'python', 'py'},
            'javascript': {'javascript', 'js'},
            'typescript': {'typescript', 'ts'},
        }
        accepted_langs = language_aliases.get(requested, {requested})
        matched_blocks = [code for lang, code in fenced_blocks if lang in accepted_langs]
        if matched_blocks:
            return '\n\n'.join(matched_blocks)

    # Fallback: if no requested language block is present, use the first fenced block.
    return fenced_blocks[0][1]


def _save_solution_to_file(question_id: str, title: str, llm_response) -> Path:
    """
    Saves the solution response from the language model to a local file.
    :param question_id:
    :param title:
    :param llm_response:
    :return:
    """
    response_content = getattr(llm_response, 'content', llm_response)
    if isinstance(response_content, list):
        response_text = '\n'.join(str(item) for item in response_content)
    elif isinstance(response_content, str):
        response_text = response_content
    else:
        response_text = str(response_content)

    source_code = _extract_code_from_response(response_text)

    file_name = f"{question_id}_{title.replace(' ', '_').lower()}"
    problems_dir = Path(__file__).resolve().parents[2] / 'content' / 'problems'
    question_dir = problems_dir / file_name

    solution_file_path = question_dir / 'solution.txt'
    solution_file_path.write_text(response_text, encoding='utf-8')

    solution_code_file_path = question_dir / 'solution.py'
    solution_code_file_path.write_text(source_code, encoding='utf-8')

    return solution_file_path


def generate(question_id: str, title: str, question: str = None) -> None:
    """
    Generates a solution for the given question using a language model and saves it to a local file.
    :param question_id:
    :param title:
    :param question:
    :return:
    """
    if question is None:
        question = get_question(question_id, title)

    model_access = os.getenv('MODEL_ACCESS', 'litellm').lower()
    if model_access == 'litellm':
        llm_model = ChatLiteLLM(
            model=os.getenv('LITELLM_DEFAULT_MODEL', 'claude-sonnet-4-6'),
        )
    else:
        llm_model = init_chat_model(
            model=os.getenv('DIRECT_DEFAULT_MODEL', 'claude-sonnet-4-6'),
        )

    llm_response = llm_model.invoke([
        SystemMessage(
            content='You are a helpful assistant that provides solutions to '
                    'data structures and algorithms questions. You will be given '
                    'a question with the detailed explanation and some valid inputs '
                    'and expected outputs. You are expected to provide a solution in '
                    'Python with the code and explanation of the code. The code should '
                    'be well formatted and should be able to run without any errors.'
                    'And easy to extract the code from the response to save to a local file.',
        ),
        HumanMessage(
            content=question,
        ),
    ])
    _save_solution_to_file(question_id, title, llm_response)


__all__ = [
    'generate',
]


def main():
    """
    Main function to generate a solution for a specific question.
    :return:
    """
    generate(question_id='2', title='Add Two Numbers')


if __name__ == '__main__':
    main()
