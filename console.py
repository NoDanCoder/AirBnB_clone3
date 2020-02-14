#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Class which control the console, and user interface """

    prompt = '(hbtn)'

    # commands

    def do_quit(self, line):
        """ Exist of the console by cmd """
        return True

    def do_EOF(self, line):
        """ Exist of the console by signal """
        return True

    def emptyline(self):
        """ Disable any action on BlankLine """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
