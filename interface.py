import actions
import keywords as kw


def handle(choice):

    KEYWORD_FUNCTION = {
        kw.HELP_KEYWORD : actions.print_help,
        kw.EXIT_KEYWORD : actions.bye
    }

    def panic():
        print("Illegal action.")

    def run():
        params = choice.split(" ")
        if not(choice in KEYWORD_FUNCTION):
            panic()
        else:
            KEYWORD_FUNCTION[choice](params)
    
    run()
    


def run():
    actions.print_welcome_message()
    while True:
        choice = input("stay-focused>>")
        handle(choice)

if __name__ == "__main__":
    run()