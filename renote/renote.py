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


# import click

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo(f"Hello {name}!")

# if __name__ == '__main__':
#     hello()



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
