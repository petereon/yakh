from yakh import get_key
from yakh.key import Keys

while True:
    key = get_key()
    if key in ['q', Keys.ENTER]:
        break
    if key.is_printable:
        print(key)