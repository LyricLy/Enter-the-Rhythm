VALID_CHARS = "1234567890qwertyuiopasdfghjklzxcvbnm_"

def map_char(c):
    if c in VALID_CHARS:
        return c
    elif c == " ":
        return "_"
    else:
        return None
