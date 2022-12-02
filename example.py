import yakh

while True:
    key = yakh.get_key()
    if key.key_codes == (3,):
        exit()
    else:
        if key.is_printable:
            print(key)
