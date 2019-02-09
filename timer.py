#timeout in minutes
class Timer():
    def __init__(self):
        self.timeout = 0
    
    def set_timeout(self, timeout):
        self.timeout = timeout

    def tick(self):
        self.timeout -= 1
    
    def is_up(self):
        return self.timeout == 0

    def run(self):
        pass      

    def alert(self):
        pass

