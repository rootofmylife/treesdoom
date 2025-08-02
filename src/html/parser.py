
class HtmlParser:

    def __init__(self, pos: int, input: str):
        self.pos = pos
        self.input = input

    def next_token(self):
        pass

    def parse_tag(self):
        pass

    def eof(self):
        return self.pos >= len(self.input)
