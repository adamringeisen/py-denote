import click
from pathlib import Path
# import subprocess
import os
from note import Note

notesDirectory: Path = Path('/home/adam/notes')
defaultNoteFormat = "md"

def getOrCreateDir(dirPath: Path):
    if dirPath.exists():
        return dirPath
    else:
        dirPath.mkdir()
    return dirPath

# 20220610T062201--define-custom-org-hyperlink-type__denote_emacs_package.md



@click.command()
def setNote():
    note = Note()  
    notesDir = getOrCreateDir(notesDirectory)
    path = notesDir / note.fileId
    with open(path, 'w') as file:
        note.printFrontMatter("mdYaml", file)
    os.system(f"xdg-open {path}")
    # subprocess.call(["nano", path])
    # sys.exit(f"File {note.fileId} created")
    

# ---
# title:      "This is a sample note"
# date:       2022-06-10
# tags:       denote  testing
# identifier: "20220610T202021"
# ---





if __name__ == "__main__":
    setNote()
