#returns a dict with lines words and characters as keys.
def statistics(fileName):
    with open(fileName, "r") as file:
        characters = len(file.read())
        file.seek(0)
        lines = file.readlines()

    return {'lines': len(lines), "words": sum(len(line.split(" ")) for line in lines), "characters": characters}