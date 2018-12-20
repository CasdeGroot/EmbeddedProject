import importlib

def create(cls):
    '''expects a string that can be imported as with a module.class name'''
    modules = cls.rsplit(".")
    module_name = modules[0]

    try:
        print('importing '+module_name)
        somemodule = importlib.import_module(module_name)
        cls_instance = getattr(somemodule, modules[1])
        i = 1
        while i < len(modules) - 1:
            i += 1
            cls_instance = getattr(cls_instance, modules[i])
            print(cls_instance)
    except Exception as err:
        print("Creating directories error: {0}".format(err))
        return None

    return cls_instance
