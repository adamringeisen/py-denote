"""Note Class."""
from datetime import datetime
import pathlib
import click


class Note:
    """A Note."""

    time: str
    idTime: str
    title: dict
    tags: dict
    fileId: str
    format_type: str
    formats: dict = {
        "mdYaml": {"ext": "md"},
        "mdToml": {"ext": "md"},
        "org": {"ext": "org"},
        "txt": {"ext": "txt"},
    }

    def __init__(self, format_type, title, tags) -> None:
        """Initialize Note."""
        self.format_type = format_type
        self.set_time(datetime.now())
        self.set_title(title)
        self.set_tags(tags)
        self.set_id()

    def create_and_open_note(self, note_dir):
        """Create and open new note."""
        path: pathlib.PurePath = note_dir / self.fileId
        with open(path, "w") as new_note_file:
            self.print_front_matter(self.format_type, new_note_file)
        click.launch(path.as_uri())

    def set_time(self, time):
        """Set time as current time of instantiation."""
        self.idTime = time.strftime("%Y%m%dT%H%M%S")
        self.time = time.strftime("%Y-%m-%d")

    def set_title(self, title):
        """Set title of Note.

        Return dict of original and formatted title.
        """
        formatted_title = "--" + title.replace(" ", "-")
        self.title = {"formatted": formatted_title, "input": title}

    def set_tags(self, tags):
        """Set tag of Note.

        Return dict of tags formated for filename
        and front matter
        """
        sortedTags = " ".join(sorted(tags.split()))
        tags = "__" + tags.replace(" ", "_")
        self.tags = {"tags": tags, "sorted": sortedTags}

    def set_id(self):
        """Construct filename for Note.

        Format is YYYYDDMMTHHMMSS--Title__tag_tag.ext
        """
        self.fileId = (
            self.idTime
            + self.title["formatted"]
            + self.tags["tags"]
            + "."
            + self.formats[self.format_type]["ext"]
        )

    def print_front_matter(self, format, file):
        """Print front matter in format to file.

        Supported formats:
        mdYaml : Markdown with Yaml flavored front matter.
        mdToml : Mardown with Toml flavored front matter.
        org : Emacs org-mode front matter. Timestamp in [inactive] form.
        txt : Plain text front matter.

        File is the file created by set_id().

        """
        match format:
            case "mdYaml":
                print(
                    "---\n"
                    f'{"title:".ljust(11)} "{self.title["input"]}"\n'
                    f'{"date:".ljust(11)} {self.time}\n'
                    f'{"tags:".ljust(11)} {self.tags["sorted"]}\n'
                    f'{"identifier:".ljust(11)} "{self.idTime}"\n'
                    "---",
                    file=file,
                )

            case "org":
                print(
                    f'{"#+title:".ljust(14)} {self.title["input"]}\n'
                    f'{"#+date:".ljust(14)} {self.time}\n'
                    f'{"#+filetags:".ljust(14)} {self.tags["sorted"]}\n'
                    f'{"#+identifier:".ljust(14)} {self.idTime}\n',
                    file=file,
                )

            case "mdToml":
                print(
                    "+++\n"
                    f'{"title".ljust(11)} = "{self.title["input"]}"\n'
                    f'{"date".ljust(11)} = {self.time}\n'
                    f'{"tags".ljust(11)} = {self.tags["sorted"]}\n'
                    f'{"identifier".ljust(11)} = "{self.idTime}"\n'
                    "+++\n",
                    file=file,
                )
            case "txt":
                print(
                    f'{"title:".ljust(11)} {self.title["input"]}\n'
                    f'{"date:".ljust(11)} {self.time}\n'
                    f'{"tags:".ljust(11)} {self.tags["sorted"]}\n'
                    f'{"identifier:".ljust(11)} {self.idTime}\n'
                    "---------------------------\n",
                    file=file,
                )
