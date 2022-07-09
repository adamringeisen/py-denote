from datetime import datetime



class Note:
    time: str
    idTime: str
    title: dict
    tags: dict
    fileId: str
    format: str
    
    def __init__(self, format, title, tags) -> None:
        self.format = format
        self.set_time()
        self.get_title(title)
        self.get_tags(tags)
        self.get_id()
        
    def set_time(self):
        time = datetime.now()
        self.idTime = time.strftime("%Y%m%dT%H%M%S")
        self.time = time.strftime("%Y-%m-%d")
    
    def get_title(self, title):
        inputTitle = title
        title = "--" + title.replace(" ", "-")
        self.title =  {"formated" : title, "input" : inputTitle}
    

    def get_tags(self, tags):
        sortedTags = ' '.join(sorted(tags.split()))
        tags = "__" + tags.replace(" ", "_")
        self.tags = {"tags" : tags, "sorted" : sortedTags}


    def get_id(self):
        self.fileId = self.idTime + self.title["formated"] + self.tags["tags"] + ".md"
        
    def print_front_matter(self, format, file):
        match format:
           case "mdYaml":
              print(
                   '---\n'
                   f'{"title:".ljust(11)} "{self.title["input"]}"\n'
                   f'{"date:".ljust(11)} {self.time}\n'
                   f'{"tags:".ljust(11)} {self.tags["sorted"]}\n'
                   f'{"identifier:".ljust(11)} "{self.idTime}"\n'
                   '---', file=file)

           case "org":
               print(
                   f'{"#+title:".ljust(14)} {self.title["input"]}\n'
                   f'{"#+date:".ljust(14)} {self.time}\n'
                   f'{"#+filetags:".ljust(14)} {self.tags["sorted"]}\n'
                   f'{"#+identifier:".ljust(14)} {self.idTime}\n'
                   , file=file)

           case "mdToml":
               print(
                   '+++\n'
                   f'{"title".ljust(11)} = "{self.title["input"]}"\n'
                   f'{"date".ljust(11)} = {self.time}\n'
                   f'{"tags".ljust(11)} = {self.tags["sorted"]}\n'
                   f'{"identifier".ljust(11)} = "{self.idTime}"\n'
                   '+++\n'
                   , file=file)
           case "txt":
               print(
                   f'{"title:".ljust(11)} {self.title["input"]}\n'
                   f'{"date:".ljust(11)} {self.time}\n'
                   f'{"tags:".ljust(11)} {self.tags["sorted"]}\n'
                   f'{"identifier:".ljust(11)} {self.idTime}\n'
                   '---------------------------\n'
                   , file=file)
               




