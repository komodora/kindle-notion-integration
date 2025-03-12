import argparse

import kindle_highlight_parser
from notion import NotionClient, define_paragraph

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="入力ファイル")
    parser.add_argument("page", help="NotionページID")
    args = parser.parse_args()
    input_file_name: str = args.input
    page_id: str = args.page

    with open(input_file_name, encoding="utf-8") as f:
        content = f.read()

    res = kindle_highlight_parser.parse_text(content)
    blocks = [define_paragraph(text) for text in res]

    nc = NotionClient()
    response = nc.append_block_children(page_id, blocks)
