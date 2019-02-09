import time
import os
#timeout in minutes
class Timer():
    def __init__(self):
        self.timeout = 0
        self.tick_message = "Remaining time: "
    
    def set_timeout(self, timeout):
        self.timeout = timeout

    def inform(self):
        os.system("clear")
        print(self.tick_message  + self.timeout.__str__())

    def tick(self):
        self.timeout -= 1
        self.inform()
    
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
        self.tick_message = "Remaining work time: "

    def alert(self):
        os.system("clear")
        print("Work done")

    

class BreakTimer(Timer):
    def __init__(self):
        self.tick_message = "Remaining break time: "

    def alert(self):
        print("Break over!")
