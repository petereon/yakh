import sys
from typing import List
from yakh.key._key import Key

try:

    import termios
    import tty
    import fcntl
    import os
    import re

    __ANSICODE = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")

    __unconsumed_chars: List[str] = []

    # Adapted from: https://stackoverflow.com/a/59159112/9019559
    def __break_on_char(imput_str: str) -> List[str]:
        pos = 0
        result = []
        for m in __ANSICODE.finditer(imput_str):
            text = imput_str[pos : m.start()]
            result.extend(list(text))
            result.append(m.group())
            pos = m.end()

        text = imput_str[pos:]
        result.extend(list(text))
        return result

    def __get_key() -> str:
        fd_input = sys.stdin.fileno()
        term_attr = termios.tcgetattr(fd_input)
        fl = fcntl.fcntl(fd_input, fcntl.F_GETFL)
        fcntl.fcntl(fd_input, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        tty.setraw(fd_input)
        ch_str = ""
        try:
            while True:
                if ch_str != "":
                    break
                while True:
                    ch_stri = sys.stdin.read(1)
                    if ch_stri == "":
                        break
                    ch_str += ch_stri
        except Exception:
            pass
        finally:
            termios.tcsetattr(fd_input, termios.TCSADRAIN, term_attr)
            fcntl.fcntl(fd_input, fcntl.F_SETFL, fl)
        first, *rest = __break_on_char(ch_str)
        __unconsumed_chars.extend(rest)
        return first

    def get_key() -> Key:
        """Returns a `Key` instance representing a keypress

        Returns:
            Key: Represents a keypress
        """
        if not __unconsumed_chars:
            ch_str = __get_key()
        else:
            ch_str = __unconsumed_chars.pop(0)

        ch_ord = tuple(map(ord, ch_str))
        return Key(ch_str, ch_ord, ch_str.isprintable() or ch_ord in [(13,), (27, 13)])

except ImportError:

    import msvcrt

    def get_key() -> Key:
        """Returns a `Key` instance representing a keypress

        Returns:
            Key: Represents a keypress
        """

        ch_str = msvcrt.getwch()
        if ch_str in ["à", "\x00"]:
            ch_str += msvcrt.getwch()
        ch_ord = tuple(map(ord, ch_str))
        return Key(ch_str, ch_ord, ch_str.isprintable())
