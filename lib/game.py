import blessed
import time


class RunningError(Exception):
    pass


class Game:
    def __init__(self, term=None):
        self.term = term or blessed.Terminal()
        self.scene = None
        self.running = False

    def start(self, scene):
        if self.running:
            raise RunningError(f"{self} is already running")

        self.scene = scene
        self.running = True
        next_render = time.time()

        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            while self.running:
                key = self.term.inkey(timeout=0, esc_delay=0)
                self.scene.on_input(self.term, key)

                t = time.time()
                if t > next_render:
                    next_render = time.time() + self.scene.render(self.term)

    def switch_scene(self, scene):
        if not self.running:
            raise RunningError(f"{self} is not running")
        self.scene = scene
