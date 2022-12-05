from unittest import mock
from ward import test
from yakh import get_key
from sys import platform

from yakh.key import Keys

if platform.startswith(("linux", "darwin", "freebsd")):

    keys_mapping = {
        b"\x01": Keys.CTRL_A,
        b"\x02": Keys.CTRL_B,
        b"\x03": Keys.CTRL_C,
        b"\x04": Keys.CTRL_D,
        b"\x05": Keys.CTRL_E,
        b"\x06": Keys.CTRL_F,
        b"\x07": Keys.CTRL_G,
        b"\x08": Keys.CTRL_H,
        b"\x09": Keys.CTRL_I,
        b"\x0a": Keys.CTRL_J,
        b"\x0b": Keys.CTRL_K,
        b"\x0c": Keys.CTRL_L,
        b"\x0d": Keys.CTRL_M,
        b"\x0e": Keys.CTRL_N,
        b"\x0f": Keys.CTRL_O,
        b"\x10": Keys.CTRL_P,
        b"\x11": Keys.CTRL_Q,
        b"\x12": Keys.CTRL_R,
        b"\x13": Keys.CTRL_S,
        b"\x14": Keys.CTRL_T,
        b"\x15": Keys.CTRL_U,
        b"\x16": Keys.CTRL_V,
        b"\x17": Keys.CTRL_W,
        b"\x18": Keys.CTRL_X,
        b"\x19": Keys.CTRL_Y,
        b"\x1a": Keys.CTRL_Z,
        b"\r": Keys.ENTER,
        b"\x1b": Keys.ESC,
        b"\t": Keys.TAB,
        b"\x1b[A": Keys.UP_ARROW,
        b"\x1b[B": Keys.DOWN_ARROW,
        b"\x1b[C": Keys.RIGHT_ARROW,
        b"\x1b[D": Keys.LEFT_ARROW,
        b"\x1b[A": Keys.NUMPAD_UP_ARROW,
        b"\x1b[B": Keys.NUMPAD_DOWN_ARROW,
        b"\x1b[C": Keys.NUMPAD_RIGHT_ARROW,
        b"\x1b[D": Keys.NUMPAD_LEFT_ARROW,
        b"\x7f": Keys.BACKSPACE,
        b"\x1b[3~": Keys.DELETE,
        b"\x1b[H": Keys.HOME,
        b"\x1b[F": Keys.END,
        b"\x1b\r": Keys.OPTION_ENTER,
    }

    for stdin_repr, key_repr in keys_mapping.items():

        @test(f"Should capture `{stdin_repr}`")
        def _(stdin_repr=stdin_repr, key_repr=key_repr):
            with mock.patch(
                "yakh._yakh.sys.stdin.buffer.raw.read",
                lambda *_, **__: stdin_repr,
            ), mock.patch(
                "yakh._yakh.termios.tcgetattr",
                lambda *_, **__: 1
            ), mock.patch(
                "yakh._yakh.tty.setraw",
                lambda *_, **__: None
            ), mock.patch(
                "yakh._yakh.termios.tcsetattr",
                lambda *_, **__: None
            ):
                assert get_key() == key_repr

elif platform in ("win32", "cygwin"):
    keys_mapping = [
        (("\x01",), Keys.CTRL_A),
        (("\x02",), Keys.CTRL_B),
        (("\x03",), Keys.CTRL_C),
        (("\x04",), Keys.CTRL_D),
        (("\x05",), Keys.CTRL_E),
        (("\x06",), Keys.CTRL_F),
        (("\x07",), Keys.CTRL_G),
        (("\x08",), Keys.CTRL_H),
        (("\x09",), Keys.CTRL_I),
        (("\x0a",), Keys.CTRL_J),
        (("\x0b",), Keys.CTRL_K),
        (("\x0c",), Keys.CTRL_L),
        (("\x0d",), Keys.CTRL_M),
        (("\x0e",), Keys.CTRL_N),
        (("\x0f",), Keys.CTRL_O),
        (("\x10",), Keys.CTRL_P),
        (("\x11",), Keys.CTRL_Q),
        (("\x12",), Keys.CTRL_R),
        (("\x13",), Keys.CTRL_S),
        (("\x14",), Keys.CTRL_T),
        (("\x15",), Keys.CTRL_U),
        (("\x16",), Keys.CTRL_V),
        (("\x17",), Keys.CTRL_W),
        (("\x18",), Keys.CTRL_X),
        (("\x19",), Keys.CTRL_Y),
        (("\x1a",), Keys.CTRL_Z),
        (("\r",), Keys.ENTER),
        (("\x1b",), Keys.ESC),
        (("\t",), Keys.TAB),
        (("à", "H"), Keys.UP_ARROW),
        (("à", "P"), Keys.DOWN_ARROW),
        (("à", "M"), Keys.RIGHT_ARROW),
        (("à", "K"), Keys.LEFT_ARROW),
        (("\x08",), Keys.BACKSPACE),
        (("à", "S"), Keys.DELETE),
        (("à", "G"), Keys.HOME),
        (("à", "O"), Keys.END),
        (("\n",), Keys.CTRL_ENTER),

        (("\x00", "H"), Keys.NUMPAD_UP_ARROW),
        (("\x00", "P"), Keys.NUMPAD_DOWN_ARROW),
        (("\x00", "M"), Keys.NUMPAD_RIGHT_ARROW),
        (("\x00", "K"), Keys.NUMPAD_LEFT_ARROW),
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
