from datetime import datetime



class Note:
    time: str
    idTime: str
    title: dict
    tags: dict
    fileId: str
    
    def __init__(self) -> None:
        self.setTime()
        self.getTitle()
        self.getTags()
        self.getID()
        
    def setTime(self):
        time = datetime.now()
        self.idTime = time.strftime("%Y%m%dT%H%M%S")
        self.time = time.strftime("%Y-%m-%d")
    
    def getTitle(self):
        inputTitle = input("Title: ")
        title = inputTitle.replace(" ", "-")
        title = "--" + title
        self.title =  {"formated" : title, "input" : inputTitle}
    

    def getTags(self):
        inputTags = input("Tags: ")
        sortedTags = ' '.join(sorted(inputTags.split()))
        tags = inputTags.replace(" ", "_")
        tags = "__" + tags.lower()
        self.tags = {"tags" : tags, "sorted" : sortedTags}


    def getID(self):
        self.fileId = self.idTime + self.title["formated"] + self.tags["tags"] + ".md"
        
    def printFrontMatter(self, format, file):
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
                   )

           case "mdToml":
               print(
                   '+++\n'
                   f'{"title".ljust(11)} = "{self.title["input"]}"\n'
                   f'{"date".ljust(11)} = {self.time}\n'
                   f'{"tags".ljust(11)} = {self.tags["sorted"]}\n'
                   f'{"identifier".ljust(11)} = "{self.idTime}"\n'
                   '+++\n'
                   )
           case "txt":
               print(
                   f'{"title:".ljust(11)} {self.title["input"]}\n'
                   f'{"date:".ljust(11)} {self.time}\n'
                   f'{"tags:".ljust(11)} {self.tags["sorted"]}\n'
                   f'{"identifier:".ljust(11)} {self.idTime}\n'
                   '---------------------------\n'
                   )
               




