import re

def parse_date(string):
    str_regex = re.compile(r"^(?P<day>(0[1-9]|[12]\d|3[0-1]))[/,.](?P<month>(0[1-9]|[1][0-2]))[/,.](?P<year>\d\d\d\d)$")
    find = str_regex.search(string)
    if find:
        dict_date = {
            "d": find.group("day"),
            "m": find.group("month"),
            "y": find.group("year")
        }
        return dict_date
    return None