#!/usr/bin/python3
""" Class of Console """

import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel



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
    def do_create(self, line):
        """Creates a new instance of BaseModel,saves it"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance = getattr(models, class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and ID"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return
        print(all_objects[key])

    def do_destroy(self, line):
        """Deletes an instance based on a class name + ID"""
        args = shlex.split(line)
        if len(args) == 0:
            print("**class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif args [0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            dict = models.storage.all()
            # Key has format <className>.id
            key = args[0] + '.' + args[1]
            if key in dict:
                del dict[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        args = shlex.split(line)
        list = []
        dict = models.storage.all()
        # show all if no class is passed
        if len(args) == 0:
            for key in dict:
                representation_Class = str(dict[key])
                list.append(representation_Class)
            # if list:
            print(list)
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            # Representation for a specific class
            representation_Class = ""
            for key in dict:
                className = key.split('.')
                if className[0] == args[0]:
                    representation_Class = str(dict[key])
                    list.append(representation_Class)
            # if list:
            print(list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        argsU = shlex.split(line)
        if len(argsU) == 0:
            print("** class name missing **")
            return
        elif len(argsU) == 1:
            print("** instance id missing **")
            return
        elif len(argsU) == 2:
            print("** attribute name missing **")
            return
        elif len(argsU) == 3:
            print("** value missing **")
            return
        elif argsU[0] not in self.classes:
            print("** class doesn't exist **")
            return
        keyI = argsU[0] + "." + argsU[1]
        dict = models.storage.all()
        try:
            instanceU = dict[keyI]
        except KeyError:
            print("** no instance found **")
            return
        try:
            type = type(getattr(instanceU, argsU[2]))
            argsU[3] = type(argsU[3])
        except AttributeError:
            pass
        setattr(instanceU, argsU[2], argsU[3])
        models.storage.save()

    def do_count(self, line):
        """Count instance"""
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        
        all_objects = models.storage.all()

        count = 0

        for key in all_objects.keys():
            name = key.split('.')[0]
            if name == class_name:
                count += 1
        print(count)

    def precmd(self, line):
        """ executed just before the command line is interpreted """
        args = line.split('.', 1)
        if len(args) == 2:
            _class = args[0]
            args = args[1].split('(', 1)
            command = args[0]
            if len(args) == 2:
                args = args[1].split(')', 1)
                if len(args) == 2:
                    _id = args[0]
                    other_arguments = args[1]
            line = command + " " + _class + " " + _id + " " + other_arguments
            return line
        else:
            return line


    def default(self, line):
        print(f"*** Unknown syntax: {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
