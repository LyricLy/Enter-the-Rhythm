import time

from lib.scene import Scene


VIEW_DISTANCE = 30


class PlayingMapScene(Scene):
    def __init__(self, game, map):
        self.game = game
        self.map = map
        map.play()
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def on_input(self, term, key):
        pass

    def draw_row_at(self, term, res):
        t = self.elapsed
        for key in self.map.keys:
            m = (key.pos - t) * res
            if m <= VIEW_DISTANCE:
                if m > -1:
                    key.render_at(term, t, res)
            else:
                # keys are in order so we can safely break early
                break

    def render(self, term):
        print(term.clear)
        with term.location(18, term.height - 12):
            self.draw_row_at(term, 36)
            print(term.move_down(1), end="")
            self.draw_row_at(term, 12)
        return 0.1
