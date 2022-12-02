from unittest import mock
from ward import test
from yakh import get_key, key
from sys import platform

if platform.startswith(("linux", "darwin", "freebsd")):

    keys_mapping = {
        b"\x01": key.CTRL_A,
        b"\x02": key.CTRL_B,
        b"\x03": key.CTRL_C,
        b"\x04": key.CTRL_D,
        b"\x05": key.CTRL_E,
        b"\x06": key.CTRL_F,
        b"\x07": key.CTRL_G,
        b"\x08": key.CTRL_H,
        b"\x09": key.CTRL_I,
        b"\x0a": key.CTRL_J,
        b"\x0b": key.CTRL_K,
        b"\x0c": key.CTRL_L,
        b"\x0d": key.CTRL_M,
        b"\x0e": key.CTRL_N,
        b"\x0f": key.CTRL_O,
        b"\x10": key.CTRL_P,
        b"\x11": key.CTRL_Q,
        b"\x12": key.CTRL_R,
        b"\x13": key.CTRL_S,
        b"\x14": key.CTRL_T,
        b"\x15": key.CTRL_U,
        b"\x16": key.CTRL_V,
        b"\x17": key.CTRL_W,
        b"\x18": key.CTRL_X,
        b"\x19": key.CTRL_Y,
        b"\x1a": key.CTRL_Z,
        b"\r": key.ENTER,
        b"\x1b": key.ESC,
        b"\t": key.TAB,
        b"\x1b[A": key.UP_ARROW,
        b"\x1b[B": key.DOWN_ARROW,
        b"\x1b[C": key.RIGHT_ARROW,
        b"\x1b[D": key.LEFT_ARROW,
        b"\x1b[A": key.NUMPAD_UP_ARROW,
        b"\x1b[B": key.NUMPAD_DOWN_ARROW,
        b"\x1b[C": key.NUMPAD_RIGHT_ARROW,
        b"\x1b[D": key.NUMPAD_LEFT_ARROW,
        b"\x7f": key.BACKSPACE,
        b"\x1b[3~": key.DELETE,
        b"\x1b[H": key.HOME,
        b"\x1b[F": key.END,
        b"\x1b\r": key.OPTION_ENTER,
    }

    for stdin_repr, key_repr in keys_mapping.items():

        @test(f"Should capture `{stdin_repr}`")
        def _(stdin_repr=stdin_repr, key_repr=key_repr):
            with mock.patch(
                "yakh._yakh.sys.stdin.buffer.raw.read",
                lambda *_, **__: stdin_repr,
            ):
                assert get_key() == key_repr

elif platform in ("win32", "cygwin"):
    keys_mapping = [
        (("\x01",), key.CTRL_A),
        (("\x02",), key.CTRL_B),
        (("\x03",), key.CTRL_C),
        (("\x04",), key.CTRL_D),
        (("\x05",), key.CTRL_E),
        (("\x06",), key.CTRL_F),
        (("\x07",), key.CTRL_G),
        (("\x08",), key.CTRL_H),
        (("\x09",), key.CTRL_I),
        (("\x0a",), key.CTRL_J),
        (("\x0b",), key.CTRL_K),
        (("\x0c",), key.CTRL_L),
        (("\x0d",), key.CTRL_M),
        (("\x0e",), key.CTRL_N),
        (("\x0f",), key.CTRL_O),
        (("\x10",), key.CTRL_P),
        (("\x11",), key.CTRL_Q),
        (("\x12",), key.CTRL_R),
        (("\x13",), key.CTRL_S),
        (("\x14",), key.CTRL_T),
        (("\x15",), key.CTRL_U),
        (("\x16",), key.CTRL_V),
        (("\x17",), key.CTRL_W),
        (("\x18",), key.CTRL_X),
        (("\x19",), key.CTRL_Y),
        (("\x1a",), key.CTRL_Z),
        (("\r",), key.ENTER),
        (("\x1b",), key.ESC),
        (("\t",), key.TAB),
        (("à", "H"), key.UP_ARROW),
        (("à", "P"), key.DOWN_ARROW),
        (("à", "M"), key.RIGHT_ARROW),
        (("à", "K"), key.LEFT_ARROW),
        (("\x08",), key.BACKSPACE),
        (("à", "S"), key.DELETE),
        (("à", "G"), key.HOME),
        (("à", "O"), key.END),
        (("\n",), key.CTRL_ENTER),

        (("\x00", "H"), key.NUMPAD_UP_ARROW),
        (("\x00", "P"), key.NUMPAD_DOWN_ARROW),
        (("\x00", "M"), key.NUMPAD_RIGHT_ARROW),
        (("\x00", "K"), key.NUMPAD_LEFT_ARROW),
    ]

    for stdin_repr, key_repr in keys_mapping:
        @test(f"Should capture `{stdin_repr}`")
        def _(stdin_repr=stdin_repr, key_repr=key_repr):
            with mock.patch(
                "yakh._yakh.msvcrt.getwch",
                side_effect=stdin_repr
            ):
                assert get_key() == key_repr
else:
    raise NotImplementedError(f"Platform `{platform}` is not supported")
