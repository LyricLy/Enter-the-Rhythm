import os

from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play

from lib.input import VALID_CHARS


class InvalidMapError(Exception):
    pass


class HitKey:
    def __init__(self, pos, char):
        self.pos = pos
        self.char = char

    def render_at(self, term, time, res):
        n = int((self.pos - time) * res)
        if n > 0:
            print(term.move_right(n) + self.char + term.move_left(n + 1), end="")
        else:
            print(term.move_left(-n) + self.char + term.move_right(-n - 1), end="")

    def __repr__(self):
        return f"Key({self.pos}, {repr(self.char)})"

class Map:
    def __init__(self, keys, song):
        self.song = song
        self.keys = keys

    @classmethod
    def from_string(cls, string, song):
        ts, o, *m = string.splitlines()
        map = "\n".join(m)
        timestep = 60 / eval(ts)
        pos = float(o)

        keys = []
        for char in map:
            if char == "\n":
                continue
            elif char == " ":
                pos += timestep
            elif char not in VALID_CHARS:
                raise ValueError(f"Map contains invalid character: {char}")
            else:
                keys.append(HitKey(pos, char))
                pos += timestep

        return cls(keys, song)

    def play(self):
        play(self.song)


def read_map(map_name):
    d = os.path.join("maps", map_name)
    song = os.path.join(d, "song.wav")
    chart = os.path.join(d, "chart.txt")

    if not os.path.exists(d):
        raise InvalidMapError(f"Map '{map_name}' not found.")
    elif not os.path.exists(song):
        raise InvalidMapError(f"Map '{map_name}' missing song.wav file.")
    elif not os.path.exists(chart):
        raise InvalidMapError(f"Map '{map_name}' missing chart.txt file.")

    with open(chart) as f:
        map = f.read()
    song = AudioSegment.from_wav(song)

    try:
        return Map.from_string(map, song)
    except ValueError:
        raise InvalidMapError(f"Map '{map_name}' failed to parse.")
