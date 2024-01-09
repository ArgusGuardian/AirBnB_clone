#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    









if __name__ == '__main__':
    HBNBCommand().cmdloop()
