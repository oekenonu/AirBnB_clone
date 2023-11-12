#!/usr/bin/python3
"""Entry point for command interpreter """
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point for command interrpreter """

    prompt = "(hbnb) "
    __classes = ["BaseModel"]


    def do_quit(self, args):
        """Quit command to exit the program """
        return True
   
    def do_EOF(self, args):
        """End program """
        return True

    def emptyline(self):
        return

    def do_create(self, arg):
        """Create new instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            instance = eval(f"{args[0]}")()
            print(instance.id)
    
    def do_show(self, arg):
        """Print String representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

if __name__ == '__main__':
    HBNBCommand().cmdloop()

