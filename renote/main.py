from datetime import datetime
from pathlib import Path

notesDirectory = Path('/home/adam/notes')


# 20220610T062201--define-custom-org-hyperlink-type__denote_emacs_package.md

def setNote():
    date = datetime.now().strftime("%Y%m%dT%H%M%S")
    title = getTitle()
    tags = getTags()
    noteID = date + title + tags + ".md"
    path = notesDirectory / noteID
    with open(path, 'w') as _:
        pass
    print(f"File created in {path}")

def getTitle():
    inputTitle = input("Title: ")
    title = inputTitle.replace(" ", "-")
    title = "--" + title
    return title

def getTags():
    inputTags = input("Tags: ")
    tags = inputTags.replace(" ", "_")
    tags = "__" + tags.lower()
    return tags

