"""CLI library."""
import click
from pathlib import Path
import configparser
from note import Note


default_notes_directory: Path = Path.home() / "notes"
config_directory: Path = Path(click.get_app_dir("renote"))
config_file: Path = config_directory / "config.ini"


def generate_default_config() -> configparser.ConfigParser:
    """Generate and return default configuration file."""
    config = configparser.ConfigParser()
    config['Options'] = {
        '# Availible Formats': 'mdYaml, mdToml, txt, org',
        'NoteFormat': 'mdYaml',
        'NoteDirectory': default_notes_directory.as_posix()
    }
    with open(config_file) as configfile:
        config.write(configfile)
    config.read(config_file)
    return config


def get_config() -> configparser.ConfigParser:
    """Get the config file."""
    config = configparser.ConfigParser()
    if not config_file.exists():
        return generate_default_config()
    else:
        config.read(config_file)
        return config


def get_or_create_dir(dir_path: Path) -> Path:
    """Get or creates a directory."""
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
    config = get_config()
    note = Note(config['Options']['NoteFormat'], title, tags)
    notes_dir = get_or_create_dir(Path(config['Options']['NoteDirectory']))
    note.create_and_open_note(notes_dir)


if __name__ == "__main__":
    main()
