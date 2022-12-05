import sys
from yakh.key._key import Key

try:

    import termios
    import tty

    def __get_key() -> bytes:
        fd_input = sys.stdin.fileno()
        term_attr = termios.tcgetattr(fd_input)
        tty.setraw(fd_input)
        ch_str = sys.stdin.read(1)
        termios.tcsetattr(fd_input, termios.TCSADRAIN, term_attr)
        return ch_str

    def get_key() -> Key:
        ch_str = __get_key()
        ch_ord = tuple(map(ord, ch_str))
        return Key(ch_str, ch_ord, ch_str.isprintable() or ch_ord in [(13,), (27, 13)])

except ImportError:

    import msvcrt

    def get_key() -> Key:
        ch_str = msvcrt.getwch()
        if ch_str in ["à", "\x00"]:
            ch_str += msvcrt.getwch()
        ch_ord = tuple(map(ord, ch_str))
        return Key(ch_str, ch_ord, ch_str.isprintable())
