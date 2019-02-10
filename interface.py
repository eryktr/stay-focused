import keywords as kw
import os
from timer import BreakTimer, WorkTimer
from actions import ActionPerformer
class Interface:

    def __init__(self):
        self.work_timer = WorkTimer(self)
        self.break_timer = BreakTimer(self)
        self.action_performer = ActionPerformer(self)

    def __handle(self, choice):
        performer = self.action_performer
        KEYWORD_FUNCTION = {
            kw.HELP_KEYWORD : performer.print_help,
            kw.EXIT_KEYWORD : performer.bye,
            kw.WORK_KEYWORD : performer.start_working_session
        }

        def panic():
            print("Illegal action.")

        def execute():
            params = choice.split(" ")
            keyword = params[0]
            if not(keyword in KEYWORD_FUNCTION):
                panic()
            else:
                KEYWORD_FUNCTION[keyword](params)
        
        execute()

    def write_line(self, line, clear = False):
        if clear:
            os.system("clear")
        print(line)
        
    def run(self):
        self.action_performer.print_welcome_message()
        while True:
            choice = input("stay-focused>>")
            try:
                self.__handle(choice)
            except Exception as e:
                error_message = str(e)
                print(error_message)

if __name__ == "__main__":
    interface = Interface()
    interface.run()