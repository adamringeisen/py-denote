"""CLI library."""
import click
from pathlib import Path

# import subprocess
import os
from note import Note

notes_directory: Path = Path(os.path.join(Path.home(), "notes"))


def get_or_create_dir(dir_path: Path):
    """Get or creates a directory."""
    if dir_path.exists():
        return dir_path
    else:
        dir_path.mkdir()
    return dir_path


@click.command()
@click.option("--format", default="mdYaml", help="Format of resulting note file")
@click.option("--title", prompt="Title", help="Title of note")
@click.option("--tags", prompt="Tags", help="Tags for note")
def main(format, title, tags):
    """Create note from arguments."""
    note = Note(format, title, tags)
    notes_dir = get_or_create_dir(notes_directory)
    path = notes_dir / note.fileId
    with open(path, "w") as file:
        note.print_front_matter(note.format, file)
    os.system(f"xdg-open {path}")


if __name__ == "__main__":
    main()
