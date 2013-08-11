import os
import fnmatch


def discover_services():
    matches = []
    dir_path = os.path.realpath('.')
    for root, dirnames, filenames in os.walk(dir_path):
        for filename in fnmatch.filter(filenames, '*.py'):
            if os.path.basename(root) == "services" and filename != "__init__.py":
                matches.append(os.path.join(root, filename))
    rel_files = [file[len(dir_path) + 1:] for file in matches]
    modules = [rel_file.replace('/', '.')[:-3] for rel_file in rel_files]
    imported_mods = [__import__(module) for module in modules]
