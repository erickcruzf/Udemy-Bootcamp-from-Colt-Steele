import re
# example parse_bytes("11010101 11100010")
def parse_bytes(string):
    binary_regex = re.compile(r"(\b[01]{8}\b)+")
    find = binary_regex.findall(string)
    return find