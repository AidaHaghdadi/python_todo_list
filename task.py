class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.is_completed = False

    def __str__(self):
        status = self.get_status()
        
        if self.description:
            return f"{self.title} | {self.description} | {status}"
        return f"{self.title} | {status}"

    def get_status(self):
        if self.is_completed:
            return "Completed"
        return "Pending"