def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode('utf-8')
    return bytes_or_str


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
