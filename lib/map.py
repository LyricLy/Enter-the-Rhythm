class InvalidMapError(Exception):
    pass


class HitKey:
    def __init__(self, pos, char):
        self.pos = pos
        self.char = char

    def render_at(self, term, time, res):
        n = int(self.pos * res)
        print(term.move_right(n) + self.char + term.move_left(n))

class Map:
    def __init__(self, song, keys):
        self.song = song
        self.keys = keys

    @classmethod
    def from_string(cls, string, song):
        
        return cls(keys, song)


def read_map(map_name):
    d = os.path.join("maps", map_name)
    song = os.path.join(d, "song.wav")
    chart = os.path.join(d, "chart.txt")

    if not os.path.exists(d):
        raise InvalidMapError(f"Map '{map_name}' not found.")
    elif not os.paths.exist(song):
        raise InvalidMapError(f"Map '{map_name}' missing song.wav file.")
    elif not os.paths.exist(chart):
        raise InvalidMapError(f"Map '{map_name}' missing chart.txt file.")

    with open(song) as f:
        map = f.read()
    return Map.from_string(map, ...)
