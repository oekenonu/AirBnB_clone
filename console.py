#!/usr/bin/python3
"""Entry point for command interpreter """
import cmd

class HBNBCommand(cmd.Cmd):
    """Entry point for command interrpreter """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program """
        return True
   
    def do_EOF(self, args):
        """End program """
        return True

    def emptyline(self):
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()

