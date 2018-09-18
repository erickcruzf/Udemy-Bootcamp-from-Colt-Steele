# Don't forget to import re!
import re
# time format example = PM "10:45", AM "3:05".
def is_valid_time(input):
    is_time = re.compile(r"^[AP]M ([0-9]|1[0-2]):(0[1-9]|[1-5][0-9])$")
    find = is_time.search(input)
    if find:
        return True
    return False
