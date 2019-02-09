import actions
import keywords as kw
from timer import Timer, WorkTimer

def handle(choice):

    KEYWORD_FUNCTION = {
        kw.HELP_KEYWORD : actions.print_help,
        kw.EXIT_KEYWORD : actions.bye,
        kw.WORK_KEYWORD : actions.start_working_session
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
    
def run():
    actions.print_welcome_message()
    while True:
        choice = input("stay-focused>>")
        try:
            handle(choice)
        except Exception as e:
            error_message = str(e)
            print(error_message)

if __name__ == "__main__":
    #run()
    timer = WorkTimer()
    timer.set_timeout(1)
    timer.run()