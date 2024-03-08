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
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        a_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                     "City": City, "Amenity": Amenity, "Place": Place,
                     "Review": Review}
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in a_classes:
            print("** class doesn't exist **")
        else:
            new_instance = a_classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and ID"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        a_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                     "City": City, "Amenity": Amenity, "Place": Place,
                     "Review": Review}
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in a_classes.keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            keys = storage.all().keys()
            key = args[0] + '.' + args[1]
            if key not in keys:
                print("** no instance found **")
                return
            objs = storage.all()
            instance = objs[key]
            print(str(instance))

    def do_destroy(self, line):
        """Deletes an instance based on a class name + ID"""
        args = shlex.split(line)
        if len(args) == 0:
            print("**class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) not in models.classes:
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
        all_objects = models.storage.all()

        if not line:
            print([str(instance) for instance in all_objects.values()])
        else:
            args = shlex.split(line)
            class_name = args[0]

            if class_name not in models.classes:
                print("** class doesn't exist **")
                return

            for instance in all_objects.values():
                if type(instance).__name__ == class_name:
                    print(str(instance))

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        a_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                     "City": City, "Amenity": Amenity, "Place": Place,
                     "Review": Review}
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in a_classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            class_id = args[1]
            obj_key = f"{class_name}.{class_id}"
            inst_keys = storage.all().keys()
            if obj_key not in inst_keys:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return

            if len(args) < 4:
                print("** value missing **")
                return

            if line[2] in ['id', 'created_at', 'updated_at']:
                return

            attr_name = args[2]
            attr_value = args[3]
            obj_dict = storage.all()[obj_key].to_dict()
            obj_dict.pop("__class__")
            obj = eval(class_name)(**obj_dict)
            if hasattr(obj, attr_name):
                type_name = type(attr_name)
                attr_value = type_name(args[3])
            setattr(obj, attr_name, attr_value)
            storage.all()[obj_key] = obj
            obj.save()

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
        """default error message"""

        print(f"*** Unknown syntax: {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
