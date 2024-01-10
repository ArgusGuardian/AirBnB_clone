#!/usr/bin/python3
import cmd
from models.base_model  import BaseModel
from models.user import User
from models import storage

def parse_arguments(arg):
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


    def do_show(self, arg):
        args = parse_arguments(arg)
        instances = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id= args[1]
            key = "{}.{}".format(args[0], id)
            if key in instances.keys():
                print(instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        args = parse_arguments(arg)
        instances = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id= args[1]
            key = "{}.{}".format(args[0], id)
            if key in instances.keys():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
    
    def do_all(self, arg):
        args = parse_arguments(arg)
        instances = storage.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = args[0]

            if class_name not in self.__classes:
                print("** class doesn't exist **")
            else:
                filtered_instances = [str(instance) for key, instance in instances.items() if key.startswith(class_name + ".")]
                if filtered_instances:
                    print(filtered_instances)
                else:
                    print("** no instance found **")

    
    def do_update(self, arg):
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
                    attribute_type = type(getattr(instance, attribute_name, None))

                    try:
                        value_str = attribute_type(value_str)
                    except ValueError:
                        return

                setattr(instance, attribute_name, value_str)
                instance.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
