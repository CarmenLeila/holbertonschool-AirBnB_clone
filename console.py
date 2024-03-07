import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def help_quit(self):
        """Print help message for the quit command"""
        print("Quit the program.")

    def help_EOF(self):
        """Print help message for the EOF command"""
        print("Exit the program when EOF is reached.")

    def help_help(self):
        """Print help message for the help command"""
        print("Get help on commands.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
