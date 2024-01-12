#!/usr/bin/python3
"""this is the console module that contains the
entry point of the command interpreter"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


def parse_arguments(arg):
    """split arguments entered in console"""
    arguments = []
    current_argument = ""
    inside_quotes = False

    for char in arg:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char.isspace() and not inside_quotes:
            if current_argument:
                arguments.append(current_argument)
                current_argument = ""
        else:
            current_argument += char

    if current_argument:
        arguments.append(current_argument)

    return arguments


class HBNBCommand(cmd.Cmd):
    """class that is in charge of every command
    passed in console"""
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

    def do_create(self, arg):
        """Creates a new instance, saves it to
        the json file and printsthe id"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            print(new.id)
            storage.save()

    def do_count(self, arg):
        """count the number of objects stored"""
        args = parse_arguments(arg)
        instances = storage.all()
        class_name = args[0]
        count = sum(1 for key in instances.keys()
                    if key.startswith(class_name + "."))
        print(count)

    def default(self, arg):
        """if the command entered in console
        doesn't exists in methods, it will search in
        this default method"""
        functions = {
            "all": 'self.do_all(args)',
            "count": 'self.do_count(args)',
            "show": 'self.do_show(args)',
            "destroy": 'self.do_destroy(args)',
            "update": 'self.do_update(args)',
        }
        list1 = re.split(r'[.,()\s]+', arg)
        args = [item for item in list1 if item]
        if len(args) >= 2:
            func = args[1]
            args.pop(1)
            args = ' '.join(args)
            if func in functions.keys():
                eval(functions[func])
            else:
                print("*** Unknown syntax: {}".format(arg))
                return False
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False

    def do_show(self, arg):
        """ Prints the string representation of
        an instance based on the class name and id"""
        args = parse_arguments(arg)
        instances = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id = args[1]
            key = "{}.{}".format(args[0], id)
            if key in instances.keys():
                print(instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id and save the change into JSON file"""
        args = parse_arguments(arg)
        instances = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id = args[1]
            key = "{}.{}".format(args[0], id)
            if key in instances.keys():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name. """
        args = parse_arguments(arg)
        instances = storage.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = args[0]

            if class_name not in self.__classes:
                print("** class doesn't exist **")
            else:
                filtered_instances = [str(instance) for key,
                                      instance in instances.items()
                                      if key.startswith(class_name + ".")]
                if filtered_instances:
                    print(filtered_instances)
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        args = parse_arguments(arg)
        instances = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]

            key = "{}.{}".format(class_name, instance_id)

            if key not in instances:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attribute_name = args[2]
                value_str = args[3]
                instance = instances[key]
                if hasattr(instance, attribute_name):
                    attribute_type = type(
                        getattr(instance, attribute_name, None))

                    try:
                        value_str = attribute_type(value_str)
                    except ValueError:
                        return

                setattr(instance, attribute_name, value_str)
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
