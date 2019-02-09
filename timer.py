import time
#timeout in minutes
class Timer():
    def __init__(self):
        self.timeout = 0
    
    def set_timeout(self, timeout):
        self.timeout = timeout

    def tick(self):
        self.timeout -= 1
    
    def is_not_up(self):
        return self.timeout > 0

    def run(self):
        while self.is_not_up():
            time.sleep(60)
            self.tick()
        self.alert()
    
    def alert(self):
        print("Timer is up")

class WorkTimer(Timer):
    def __init__(self):
        super().__init__()

    def alert(self):
        print("Work done")

class BreakTimer(Timer):
    def __init__(self):
        super().__init__()

    def alert(self):
        print("Break over!")
