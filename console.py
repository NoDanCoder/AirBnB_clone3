#!/usr/bin/python3
""" Entry point of the command interpreter """
import subprocess
from cmd import Cmd


class Console(Cmd):
    """ Class which control the console, and user interface """

    prompt = '(hbtn)'

    def default(self, line):  # this method will catch all commands
        subprocess.call(line, shell=True)


if __name__ == '__main__':
    Console().cmdloop()
