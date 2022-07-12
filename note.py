"""Datetime for dates."""
from datetime import datetime
import os


class Note:
    """Single Note."""

    time: str
    idTime: str
    title: dict
    tags: dict
    fileId: str
    format_type: str
    formats: dict = {
        "mdYaml": {"ext": "md", "desc": "Markdown with Yaml Flavored Front Matter"},
        "mdToml": {"ext": "md", "desc": "Markdown with Toml Flavored Front Matter"},
        "org": {
            "ext": "org",
            "desc": "Emacs org-mode front matter. Timestamp in [inactive] form.",
        },
        "txt": {"ext": "txt", "desc": "Plain text front matter."},
    }

    def __init__(self, format_type, title, tags) -> None:
        """Initialize Note."""
        self.format_type = format_type
        self.set_time()
        self.get_title(title)
        self.get_tags(tags)
        self.get_id()

    def create_and_open_note(self, note_dir):
        """Create and open new note."""
        path = note_dir / self.fileId
        with open(path, "w") as new_note_file:
            self.print_front_matter(self.format_type, new_note_file)
        os.system(f"xdg-open {path}")

    def set_time(self):
        """Set time as current time of instantiation."""
        time = datetime.now()
        self.idTime = time.strftime("%Y%m%dT%H%M%S")
        self.time = time.strftime("%Y-%m-%d")

    def get_title(self, title):
        """Set title of Note.

        Return dict of original and formatted title.
        """
        inputTitle = title
        title = "--" + title.replace(" ", "-")
        self.title = {"formated": title, "input": inputTitle}

    def get_tags(self, tags):
        """Set tag of Note.

        Return dict of tags formated for filename
        and front matter
        """
        sortedTags = " ".join(sorted(tags.split()))
        tags = "__" + tags.replace(" ", "_")
        self.tags = {"tags": tags, "sorted": sortedTags}

    def get_id(self):
        """Construct filename for Note.

        Format is YYYYDDMMTHHMMSS--Title__tag_tag.ext
        TODO: Extension currently ugly.
        """
        self.fileId = (
            self.idTime
            + self.title["formated"]
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
