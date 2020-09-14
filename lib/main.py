import os

from lib.scene import Scene


class MainMenuScene(Scene):
    def __init__(self):
        self.selected = 0
        self.top()

    def on_input(self, term, key):
        if key.code == term.KEY_UP and self.selected > 0:
            self.selected -= 1
        elif key.code == term.KEY_DOWN and self.selected < len(self.choices)-1:
            self.selected += 1
        elif key.code == term.KEY_ENTER:
            print(term.clear)
            self.choices[self.selected][1]()

    def render(self, term):
        block = [self.header, ""]
        for i, (s, _) in enumerate(self.choices):
            if i == self.selected:
                s = term.reverse(s)
            block.append(s)

        start = term.height // 2 - len(block) // 2
        with term.location(y=start):
            for line in block:
                print(term.center(line))
        return 0

    def top(self):
        self.header = "Menu"
        self.choices = [
            ("Select Map", self.play),
            ("Options", self.options),
        ]

    def play(self):
        self.header = "Select a map"
        self.choices = []
        for m in os.listdir("maps"):
            self.choices.append((m, self.dispatch(m)))
        self.choices.append(("Back", self.top))

    def dispatch(self, title):
        def _inner():
            pass
        return _inner

    def options(self):
        self.header = "Options"
        self.choices = [
            ("Nothing here!", lambda: None),
            ("Back", self.top),
        ]
