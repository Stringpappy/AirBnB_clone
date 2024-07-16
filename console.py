#!/usr/bin/python3
""" HBNB programme AirBnB Console """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNB General Class"""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """ func that Exit  quit programme """
        exit()

    def do_EOF(self, arg):
        """ Func that  Exit method for EOF """
        print('')
        exit()

    def emptyline(self):
        """ The Func to pass when emptyline entered """
        pass

    def do_create(self, arg):
        """ Func that Create a new instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        rec = None
        if arg:
            list_of_arg = arg.split()
            if len(list_of_arg) == 1:
                if arg in self.classes.keys():
                    rec = self.classes[arg]()
                    rec.save()
                    print(rec.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ func  to print instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """the func that delete instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        list_of_arg = arg.split()
        try:
            obj = eval(list_of_arg[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(list_of_arg) == 1:
            print('** instance id missing **')
            return
        if len(list_of_arg) > 1:
            key = arg_list_of_arg[0] + '.' + list_of_arg[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """ func to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_update(self, arg):
        """ func to update JSON file"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
