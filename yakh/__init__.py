from yakh._yakh import get_key
from yakh import key


"""
# yakh

yakh (Yet Another Keypress Handler) tries to handle keypresses from the stdin in the terminal in high-level platform indepdendent manner.

## Usage

```python
from yakh import get_key
from yakh.key import Keys

key = ''
while key not in ['q', Keys.ENTER]:
    key = get_key()
    if key.is_printable:
        print(key)
```

yakh is dead-simple, there is only one function `get_key()` which takes no arguments and blocks until a key is pressed.

For each keypress it creates an instance of [`Key`](./yakh/key/_key.py#L7) which holds:

- `.key`: characters representing the keypress
- `.key_codes`: collection of Unicode code point encodings for all the characters (given by `ord` function)
- `.is_printable`: printability of the characters in the keypress

Additionally `Key` instances

-  are comparable with another `Key` instances, `str` instances and *Unicode code point* representations (tuples of integers)
- come with string representation for purposes of printing and string concatenation, which returns the content of `.key` attribute

## `yakh.key` submodule
`yakh.key` sub-module contains platform dependent representations of certain keys under `Keys` class. These are available namely for `CTRL` key combinations and some other common keys. 

Full list of keys can be seen [here](./yakh/key/_key.py#L42) and [here](./yakh/key/_key.py#L81).
"""
