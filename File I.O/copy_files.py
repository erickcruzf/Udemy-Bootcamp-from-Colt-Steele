fileName = "story.txt"
newFileName = "story_copy.txt"

def copy(fileName, newFileName):
    with open(fileName, "r") as file:
        content = file.read()
    with open(newFileName, "w") as file:
        file.write(content)