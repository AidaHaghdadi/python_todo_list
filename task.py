class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.is_completed = False

    def __str__(self):
        return self.title