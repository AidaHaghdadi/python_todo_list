class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False

    def __str__(self):
        return self.title