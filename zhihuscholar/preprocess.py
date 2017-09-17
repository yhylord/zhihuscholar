from bs4 import BeautifulSoup
from zhihu_scholar.chinese_segmenter import chinese_segmenter


def get_html(filename):
    with open(filename, 'r') as f:
        return f.read()


def extract_text(html_article):
    soup = BeautifulSoup(html_article, 'html.parser')
    return soup.get_text()


def remove_control_characters(text):
    removal_table = {ord(c): None for c in '\n\t'}
    return text.translate(removal_table)


def tokenize(text):
    segments = chinese_segmenter.cut(text)
    return ' '.join(map(lambda x: x[0], segments))


def preprocess(filename):
    html = get_html(filename)
    text = extract_text(html)
    pure_text = remove_control_characters(text)
    tokenized_text = tokenize(pure_text)
    return tokenized_text