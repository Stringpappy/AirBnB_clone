#!/usr/bin/python3
"""

The progtamme that Defines the HBNB console.

"""
import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The func that Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """The func that Ignore empty spaces."""
        pass

    def do_quit(self, line):
        """The func that Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """The func EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """The func that Create a new class instance
        with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
        listmi = line.split(" ")
        kwargs = {}
        for itr in range(1, len(listmi)):
            key, value = tuple(listmi[itr].split("="))
            if value[0] == '"':
                value = value.strip('"').replace("_", " ")
            else:
                try:
                    value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                    kwargs[key] = value

            if kwargs == {}:
                myobj = eval(listmi[0])()
            else:
                myobj = eval(listmi[0])(**kwargs)
                storage.new(myobj)
            print(myobj.id)
            myobj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        The func that Prints the string representation of an instance
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        The func that Deletes an instance based on the class name and id
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        if not line:
            store = storage.all()
            print([store[k].__str__() for k in store])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError()

            store = storage.all(eval(args[0]))
            print([store[k].__str__() for k in store])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """func that Updates an instanceby adding or updating attribute
        """
        try:
            if not line:
                raise SyntaxError()
            m_list = split(line, " ")
            if m_list[0] not in self.__classes:
                raise NameError()
            if len(m_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = m_list[0] + '.' + m_list[1]
            if key not in objects:
                raise KeyError()
            if len(m_list) < 3:
                raise AttributeError()
            if len(m_list) < 4:
                raise ValueError()
            t = objects[key]
            try:
                t.__dict__[m_list[2]] = eval(m_list[3])
            except Exception:
                t.__dict__[m_list[2]] = m_list[3]
                t.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, line):
        """
        func that count the number of instances of a class
        """
        ctr = 0
        try:
            my_list = split(line, " ")
            if my_list[0] not in self.__classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == my_list[0]:
                    ctr += 1
            print(ctr)
        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """
        func that strips the argument and return a string of command
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """
        func that retrieve all instances of a class and
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
