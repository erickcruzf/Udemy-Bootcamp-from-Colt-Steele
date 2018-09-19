import re

def censor(string):
    pattern = re.compile(r"(\w*frack\w*)", re.I)
    return pattern.sub("CENSORED", string)

print(censor("youfrackingmonster"))