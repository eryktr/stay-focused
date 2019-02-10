import time
import os
import abc

#timeout in minutes
class Timer(abc.ABC):
    def __init__(self, interface):
        self.timeout = 0
        self.interface = interface
    
    def set_timeout(self, timeout):
        self.timeout = timeout

    @abc.abstractmethod
    def inform(self):
        pass

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
    
    @abc.abstractmethod
    def alert(self):
        pass


class WorkTimer(Timer):
    def __init__(self, interface):
        super().__init__(interface)
        self.tick_message = "Remaining work time: "

    def alert(self):
        os.system("clear")
        self.interface.write_line("Work done")

    def inform(self):
        os.system("clear")
        self.interface.write_line("work tick")

        
class BreakTimer(Timer):
    def __init__(self, interface):
        super().__init__(interface)
        self.tick_message = "Remaining break time: "

    def alert(self):
        os.system("clear")
        self.interface.write_line("Break over!")

    def inform(self):
        os.system("clear")
        self.interface.write_line("break tick")
