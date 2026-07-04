"""
Extracts the question content from LeetCode using the GraphQL API.
"""

import html
import re
import requests


def _html_to_plain_text(content_html: str) -> str:
    """
    Converts HTML content to plain text by removing tags and normalizing whitespace.
    :param content_html: string containing HTML content
    :return: string containing plain text
    """
    text: str = content_html or ''

    # Convert common block tags into line breaks before stripping tags.
    text = re.sub(r'<\s*br\s*/?\s*>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<\s*/\s*p\s*>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<\s*/\s*pre\s*>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<\s*pre\s*>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<\s*li[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<\s*/\s*li\s*>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<\s*/\s*ul\s*>', '\n', text, flags=re.IGNORECASE)

    # Strip all remaining HTML tags and decode entities.
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text).replace('\xa0', ' ')

    normalized_lines: list[str] = []
    for line in text.splitlines():
        cleaned = re.sub(r'\s+', ' ', line).strip()
        normalized_lines.append(cleaned)

    text = '\n'.join(normalized_lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'\n(Example \d+:|Constraints:|Follow-up:)', r'\n\n\1', text)
    text = re.sub(r'\n\n+(?=(-?\d|Only one valid answer exists\.))', '\n', text)

    return text.strip()


def _format_question_text(frontend_id: str, title: str,
                          difficulty: str, description_html: str) -> str:
    """
    Formats the question text by combining the frontend ID, title, difficulty, and description.
    :param frontend_id:
    :param title:
    :param difficulty:
    :param description_html:
    :return:
    """
    body: str = _html_to_plain_text(description_html)
    return f'{frontend_id}. {title}\n\nDifficulty: {difficulty}\n\n{body}'.strip()


def extract(title_slug) -> dict[str, str]:
    """
    Extracts the question content from LeetCode using the GraphQL API.
    :param title_slug:
    :return:
    """
    url: str = 'https://leetcode.com/graphql/'

    # GraphQL query asking specifically for the question content
    query: str = """
    query questionContent($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
            content
            mysqlSchemas
            dataSchemas
        }
    }
    """

    variables: dict[str, str] = {'titleSlug': title_slug}
    headers: dict[str, str] = {
        'Content-Type': 'application/json',
        'Referer': f'https://leetcode.com/problems/{title_slug}/',
        'User-Agent': 'Mozilla/5.0',
    }

    response: requests.Response = requests.post(
        url,
        json={'query': query, 'variables': variables},
        headers=headers,
        timeout=20,
    )

    if response.status_code != 200:
        return {
            'error': f'Error: Status code {response.status_code}, body: {response.text[:200]}',
        }

    data: dict = response.json()
    if data.get('data') and data['data'].get('question'):
        question = data['data']['question']
        return {
            'content': _format_question_text(
                question.get('questionFrontendId', ''),
                question.get('title', ''),
                question.get('difficulty', ''),
                question.get('content', ''),
            ),
            'id': question.get('questionFrontendId', ''),
            'title': question.get('title', ''),
        }

    return {
        'error': 'Error: Problem not found.',
    }


__all__ = [
    'extract',
]


def main():
    """
    Main function to test the extract_question function with a specific LeetCode problem slug.
    :return:
    """
    slug: str = 'longest-palindromic-substring'
    print(extract(slug))


if __name__ == '__main__':
    main()
