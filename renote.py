import click
from pathlib import Path
# import subprocess
import os
from note import Note

notesDirectory: Path = Path.home()
defaultNoteFormat = "md"

def getOrCreateDir(dirPath: Path):
    if dirPath.exists():
        return dirPath
    else:
        dirPath.mkdir()
    return dirPath


@click.command()
@click.option('--format', default="mdYaml", help="Format of resulting note file")
@click.option('--title', prompt="Title", help="Title of note")
@click.option('--tags', prompt="Tags", help='Tags for note')
def setNote(format, title, tags):  
    note = Note(format, title, tags)  
    notesDir = getOrCreateDir(notesDirectory)
    path = notesDir / note.fileId
    with open(path, 'w') as file:
        note.printFrontMatter(note.format, file)
    os.system(f"xdg-open {path}")
    # subprocess.call(["nano", path])
    # sys.exit(f"File {note.fileId} created")
   
if __name__ == "__main__":
    setNote()
