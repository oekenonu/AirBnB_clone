#!/usr/bin/python3
"""Entry point for command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Entry point for command interrpreter """

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User"]


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

    def do_destroy(self, arg):
        """Destroy an instance"""
        args = arg.split()
        if len(args) == 0 :
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
        storage.save()
    
    def do_all(self, arg):
        """Retuns all instances representation"""
        args = arg.split()

        if len(arg) == 0:
            print([str(val) for val in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if k.startswith(args[0])])


    def do_update(self, arg):
        """Update an Instance Based on the class name & id"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")    
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

