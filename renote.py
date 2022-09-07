"""CLI library."""
import click
from pathlib import Path
import configparser
import os
from note import Note

notes_directory: Path = Path(os.path.join(Path.home(), "notes"))


def generate_default_config(path: Path):
    """Generate a default configuration file."""
    config = configparser.ConfigParser()
    config['Options'] = {
        'NoteFormat': 'mdYaml',
        'NoteDirectory': notes_directory.as_posix()
    }
    with open(os.path.join(path, "config.ini"), 'w') as configfile:
        config.write(configfile)


def get_config():
    """Get the config file."""
    config_dir = Path(click.get_app_dir("renote"))
    if config_dir.exists():
        print("Dir exists!")
    else:
        config_dir.mkdir()
        generate_default_config(config_dir)


def get_or_create_dir(dir_path: Path):
    """Get or creates a directory.

    Will be replaced by config at some point.
    """
    if dir_path.exists():
        return dir_path
    else:
        dir_path.mkdir()
    return dir_path


@click.command()
@click.option("--format",
              default="mdYaml",
              help="Format of resulting note file")
@click.option("--title", prompt="Title", help="Title of note")
@click.option("--tags", prompt="Tags", help="Tags for note")
def main(format, title, tags):
    """Create note from arguments."""
    get_config()
    # note = Note(format, title, tags)
    # notes_dir = get_or_create_dir(notes_directory)
    # note.create_and_open_note(notes_dir)


if __name__ == "__main__":
    main()
