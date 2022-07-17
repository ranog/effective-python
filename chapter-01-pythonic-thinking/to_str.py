def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode('utf-8')
    return bytes_or_str


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))
