import dataclasses
from enum import Enum


class HighlightColor(Enum):
    BLUE = ("青色", "🔵")
    PINK = ("ピンク色", "🔴")
    ORANGE = ("オレンジ色", "🟠")
    YELLOW = ("黄色", "🟡")

    def __init__(self, prefix, mark):
        self.PREFIX = prefix
        self.MARK = mark


def which_highlight_color(text: str):
    for color in HighlightColor:
        if text.startswith(color.PREFIX):
            return color


@dataclasses.dataclass
class Highlight:
    color: HighlightColor
    text: str

    def __str__(self):
        return f"{self.color.MARK} {self.text}"

    def get_str(self):
        return self.__str__()


def parse_text(content: str):
    lines = list(filter(str.strip, content.split("\n")))
    result: list[str] = []

    for color, text in zip(lines[::2], lines[1::2]):
        trimmed_text = text.rstrip("\n").replace(" ", "").replace("\u3000", "")

        if (hl_color := which_highlight_color(color)) is None:
            continue
        hl = Highlight(color=hl_color, text=trimmed_text)
        result.append(hl.get_str())

    return result
