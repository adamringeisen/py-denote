from datetime import datetime
from pathlib import Path
import os


notesDirectory = Path('/home/adam/notes')


def getOrCreateDir(dirPath):
    if dirPath.exists():
        return dirPath
    else:
        dirPath.mkdir()
    return dirPath

# 20220610T062201--define-custom-org-hyperlink-type__denote_emacs_package.md


def setNote():
    dateNow = datetime.now()
    dateID = dateNow.strftime("%Y%m%dT%H%M%S")
    date = dateNow.strftime("%Y %m %d")
    title = getTitle()
    tags = getTags()
    noteID = dateID + title[0] + tags[0] + ".md"
    notesDir = getOrCreateDir(notesDirectory)
    path = notesDir / noteID
    with open(path, 'w') as file:
        file.writelines(
            mdFrontMatter(title[1], date, tags[1], dateID)
        )
    os.system(f"emacs {path}")


def getTitle():
    inputTitle = input("Title: ")
    title = inputTitle.replace(" ", "-")
    title = "--" + title
    return [title, inputTitle]


def getTags():
    inputTags = input("Tags: ")
    sortedTags = ' '.join(sorted(inputTags.split()))
    tags = inputTags.replace(" ", "_")
    tags = "__" + tags.lower()
    return [tags, sortedTags]

# ---
# title:      "This is a sample note"
# date:       2022-06-10
# tags:       denote  testing
# identifier: "20220610T202021"
# ---


def mdFrontMatter(title, date, tags, id):
    return f'''---
{"title:".ljust(11)} "{title}"
{"date:".ljust(11)} {date}
{"tags:".ljust(11)} {tags}
{"identifier:".ljust(11)} "{id}"
---'''


def AddFrontMatter(type):
    pass


if __name__ == "__main__":
    setNote()
