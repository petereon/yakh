from typing import Tuple, Union
from sys import platform

"""yakh.key` sub-module contains `Key` class which is used to represent keypresses and platform dependent representations of certain keys under `Keys` class. These are available namely for `CTRL` key combinations and some other common keys. 
"""


class Key:
    """`Key` class is used to represent keypresses

    Raises:
        ValueError: Raised when comparison is not possible
    """

    key: str
    key_codes: Tuple[int, ...]
    is_printable: bool

    def __init__(self, key: str, key_codes: Tuple[int, ...], is_printable: bool):
        self.key = key
        self.key_codes = key_codes
        self.is_printable = is_printable

    def __str__(self):
        return self.key

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: Union[Tuple[int, ...], str]):
        if isinstance(other, str):
            return self.key == other

        if isinstance(other, tuple) and all(isinstance(item, int) for item in other):
            return self.key_codes == other

        if isinstance(other, Key):
            return all(
                [
                    self.key == other.key,
                    self.key_codes == other.key_codes,
                    self.is_printable == other.is_printable,
                ]
            )

        raise ValueError(f"Cannot compare with {other}. Expected `List[int]` or `str`.")

    def __ne__(self, other):
        return not self.__eq__(other)


class _PlatformIndependentKeys:
    CTRL_A = (1,)
    CTRL_B = (2,)
    CTRL_C = (3,)
    CTRL_D = (4,)
    CTRL_E = (5,)
    CTRL_F = (6,)
    CTRL_G = (7,)
    CTRL_H = (8,)
    CTRL_I = (9,)
    CTRL_J = (10,)
    CTRL_K = (11,)
    CTRL_L = (12,)
    CTRL_M = (13,)
    CTRL_N = (14,)
    CTRL_O = (15,)
    CTRL_P = (16,)
    CTRL_Q = (17,)
    CTRL_R = (18,)
    CTRL_S = (19,)
    CTRL_T = (20,)
    CTRL_U = (21,)
    CTRL_V = (22,)
    CTRL_W = (23,)
    CTRL_X = (24,)
    CTRL_Y = (25,)
    CTRL_Z = (26,)

    ENTER = (13,)
    ESC = (27,)

    TAB = (9,)

    def __init__(self):
        raise RuntimeError("`Keys` class cannot be instatiated")


if platform.startswith(("linux", "darwin", "freebsd")):

    class Keys(_PlatformIndependentKeys):
        UP_ARROW = (27, 91, 65)
        DOWN_ARROW = (27, 91, 66)
        RIGHT_ARROW = (27, 91, 67)
        LEFT_ARROW = (27, 91, 68)

        NUMPAD_UP_ARROW = (27, 91, 65)
        NUMPAD_DOWN_ARROW = (27, 91, 66)
        NUMPAD_RIGHT_ARROW = (27, 91, 67)
        NUMPAD_LEFT_ARROW = (27, 91, 68)

        BACKSPACE = (127,)
        DELETE = (27, 91, 51, 126)

        HOME = (27, 91, 72)
        END = (27, 91, 70)

        OPTION_ENTER = (27, 13)
        CTRL_ENTER = OPTION_ENTER

elif platform in ("win32", "cygwin"):

    class Keys(_PlatformIndependentKeys):
        UP_ARROW = (224, 72)
        DOWN_ARROW = (224, 80)
        RIGHT_ARROW = (224, 77)
        LEFT_ARROW = (224, 75)

        NUMPAD_UP_ARROW = (0, 72)
        NUMPAD_DOWN_ARROW = (0, 80)
        NUMPAD_RIGHT_ARROW = (0, 77)
        NUMPAD_LEFT_ARROW = (0, 75)

        BACKSPACE = (8,)
        DELETE = (224, 83)

        HOME = (224, 71)
        END = (224, 79)

        CTRL_ENTER = (10,)
        OPTION_ENTER = CTRL_ENTER

else:
    raise NotImplementedError(f"Platform `{platform}` is not supported")
