import inspect
import importlib

# This class is used to get the information of a module
class package:

    # Constructor, load the module by name
    def __init__(self, name):
        self.module = importlib.import_module(name)

    # Get the submodules of a module, recursively
    def get_modules(self, obj):
        modules = inspect.getmembers(obj, inspect.ismodule)
        list = []
        for m in modules:
            if( m[1].__name__.startswith(obj.__name__+'.') ):
                list.append(self.get_members(m[1]))
        return list

    # Get the classes of a module
    def get_classes(self, obj):
        classes = inspect.getmembers(obj, inspect.isclass)
        return [c[0] for c in classes]

    # Get the functions of a module
    def get_functions(self, obj):
        functions = inspect.getmembers(obj, inspect.isfunction)
        return [ f[1] for f in functions]

    # Get the members of a module
    def get_members(self, obj):
        modules = self.get_modules(obj)
        classes = self.get_classes(obj)
        functions = self.get_functions(obj)
        return { obj.__name__: modules, 'classes': classes, 'functions': functions }

    # Get full information of a module, including submodules, classes and functions
    def get_package_info(self):
        return self.get_members(self.module)    