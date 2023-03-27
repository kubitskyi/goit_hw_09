
PHONE_NUMBER = {'cail':"380971111111"}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me name, old phone and new phone"
        except KeyError:
            return "Enter correct username"
        except ValueError:
            return "Enter username"
        except TypeError:  
            return "Not enough params for command"
    return inner

@input_error
def hello(*args):
    return "How can I help you?"

def help(*args):
    return"""Tthis is an instruction"""

@input_error
def add_phone(*args):
    lst_param = args[0].split()
    name = lst_param[0]
    phone = lst_param[1]
    PHONE_NUMBER.update({name: phone})
    return f'{name.capitalize()}: {phone}'

@input_error
def change_phone(*args):
    lst_param = args[0].split()
    name = lst_param[0]
    phone = lst_param[1]
    PHONE_NUMBER[name] = phone
    return f'{name.capitalize()}: {phone}'

@input_error
def show_phone(*args):
    return PHONE_NUMBER[args[1]]


def show_all(*args):
    return '\n'.join([k+": "+ v for k, v in PHONE_NUMBER.items()])

@input_error
def exit(*args):
    return 'Bay'

COMMANDS = {help: 'help',
            add_phone: 'add',
            show_phone: "show",
            change_phone: "change",
            show_all: "all",
            exit: 'exit'}

def command_handler(text: str):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            
            return command, text.replace(kword, '').strip()
    return None, None


def main():
    while True:
        user_input = input('>>>')

        command, data = command_handler(user_input)
        print(command(data))
        if command == exit:
            break
     

        

if __name__=="__main__":
    main()