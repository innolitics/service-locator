from os import path
import glob


def discover_services(search_path):
    """

    :param search_path: the absolute path to the root of the project. All services folders will be found
    and their python files imported relative to the project root.
    :return: nothing
    """

    dir_path = path.dirname(search_path)
    files = glob.glob(path.join(dir_path, '**/services/*.py'))

    rel_files = [file[len(dir_path) + 1:] for file in files if path.basename(file) != "__init__.py"]
    modules = [rel_file.replace('/', '.')[:-3] for rel_file in rel_files]
    print("imported", modules)
    imported_mods = [__import__(module) for module in modules]
