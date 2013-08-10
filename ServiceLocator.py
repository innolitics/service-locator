import os
import glob

_lookup = {}


def ServiceProvider(*services):
    """
    This is a class decorator that declares a class to provide a set of services.
    It is expected that the class has a no-arg constructor and will be instantiated
    as a singleton.
    """

    def realDecorator(clazz):
        instance = clazz()
        for service in services:
            list = _lookup.get(service)
            if not list:
                list = []
                _lookup[service] = list
            list.append(instance)
        return clazz

    return realDecorator


def locate_all(service):
    list = _lookup.get(service) or []
    return list


def locate(service):
    try:
        return locate_all(service)[0]
    except IndexError:
        return None


def discover_services(search_path):
    dir_path = os.path.dirname(search_path)
    files = glob.glob(os.path.join(dir_path, '**/services/*.py'))
    rel_files = [file[len(dir_path) + 1:] for file in files]
    modules = [rel_file.replace('/', '.')[:-3] for rel_file in rel_files]
    imported_mods = [__import__(module) for module in modules]
