#!/usr/bin/python3
""" Class of Console """

import cmd
import shlex
import models

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

    def do_create(self, argument):
        """creates a new instance of BaseModel and saves it """
        if not argument:
            print("** class name missing **")
            return
        class_name = argument[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        new_instance = getattr(models, class_name) ()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, argument):
        """prints the string representation of an instance """
        if not argument:
            print("** class name missing **")
            return

        if argument[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(argument) < 2:
            print("** instance id missing **")
            return

        instance_id = argument[1]
        try:
            instance = models.get(instance_id)
            print(instance)
        except:
            print("** no instance found **")

    def do_destroy(self, argument):
        """ deletes an instance based on the class name and ID """
        if not argument:
            print("** class name missing **")
            return

        if argument[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(argument) < 2:
            print("** instance id missing **")
            return

        instance_id = argument[1]
        try:
            instance = models.get(instance_id)
            instance.delete()
            models.save_to_file()
        except:
            print("** no instance found **")

    def do_all(self, argument):
        """prints all string representation of all instances"""
        if argument and argument[0] not in models.classes:
            print("** class doesn't exist **")
            return

        instances = models.all()
        print([str(instance) for instance in instances])

    def do_update(self, argument):
        """Updates an instance based on the class name and ID"""
        if not argument:
            print("** class name missing **")
            return

        if argument[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(argument) < 2:
            print("** instance id missing **")
            return

        instance_id = argument[1]
        try:
            instance = models.get(instance_id)
        except:
            print("** no instance found **")
            return

        if len(argument) < 4:
            print("** attribute name missing **")
            return

        attribute_name = argument[2]
        if len(argument) < 5:
            print("** value missing **")
            return

        attribute_value = argument[3]

        if hasattr(instance, attribute_name):
            # Convert attribute value to the attribute type
            attribute_type = type(getattr(instance, attribute_name))
            try:
                setattr(instance, attribute_name, attribute_type(attribute_value))
                instance.save()
            except:
                print("** value must be of type {} **".format(attribute_type.__name__))
        else:
            print("** attribute name doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
