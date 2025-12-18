from datetime import datetime

class Todo:
    def __init__(self, task):
        self.task = task              # variabel
        self.datetime = None
        self.done = False

    def set_datetime(self, dt):       # function
        self.datetime = dt

    def mark_done(self):
        self.done = True
