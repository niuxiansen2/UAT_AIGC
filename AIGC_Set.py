# coding=utf-8
import streamlit as st
import markdown
from markupsafe import Markup


# md转html的方法
def md2html(markdown_file):
    with open(markdown_file, "r") as file:
        content = file.read()
    return content

    # html = markdown.markdown(mdContent, extensions=exts)
    # content = Markup(html)
    # return mdContent


import re


def generate_toc(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    toc = []
    header_pattern = re.compile(r'^(#{1,6})\s*(.+)')
    for line in content:
        match = header_pattern.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            link = re.sub(r'[^\w\s-]', '', title).replace(' ', '-').lower()
            toc.append(f"{'  ' * (level - 1)}- [{title}](#{link})")

    return '\n'.join(toc)


# 使用示例


def AIGC_SET():
    st.header("🛒AIGC应用合集", divider="rainbow")
    st.markdown(md2html('./fileSource/AIGC合集.md'), unsafe_allow_html=False)


if __name__ == '__main__':
    md_file_path = './fileSource/AIGC合集.md'
    toc = generate_toc(md_file_path)
    print(toc)
