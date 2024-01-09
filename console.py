#!/usr/bin/python3
import cmd
from models.base_model  import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_help(self, arg):
        """This is the help command"""
        return super().do_help(arg)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass
    
    def do_create(self,arg):
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            print(new.id)
            storage.save()


    def do_show(self, *args):
        instance = eval((args[0])().arg[1])
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif not args[1]:
            print("** instance id missing **")
        elif not instance:
            print("** no instance found **")
        else:
            print(instance)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
