import cmd
import models.base_model import BaseModel
class HBNBCommand(cmd.Cmd):
    """for quiting the programm"""
    prompt = 'hbnb()'

    def do_quit(self, arg):
        """end file"""
        return True

    def do_EOF(self, *arg):
        """empty file"""
        return True

    def do_create(self,line):
        """create instance"""
        if not line:
            prit("** class name missing **")
            return
        if line in models:
            new_instance = models[line]()
            new_instance.save()
            print(new_instance.id)
            return

        print("create method is called")
    
    def do_emptyline(self):
        ""empty file"""
        pass
