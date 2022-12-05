import sys
from yakh.key._key import Key

try:

    import termios, tty

    fdInput = sys.stdin.fileno()
    termAttr = termios.tcgetattr(0)

    def __get_key() -> bytes:
        tty.setraw(fdInput)
        ch = sys.stdin.read(1)
        termios.tcsetattr(fdInput, termios.TCSADRAIN, termAttr)
        return ch

    def get_key() -> Key:
        ch = __get_key()
        ch_ord = tuple(map(ord, ch))
        return Key(ch, ch_ord, ch.isprintable() or ch_ord in [(13,), (27, 13)])

except ImportError:

    import msvcrt

    def get_key() -> Key:
        ch = msvcrt.getwch()
        if ch in ["à", "\x00"]:
            ch += msvcrt.getwch()
        ch_ord = tuple(map(ord, ch))
        return Key(ch, ch_ord, ch.isprintable())
