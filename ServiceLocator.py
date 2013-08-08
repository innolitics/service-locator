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


def LocateAll(service):
    list = _lookup.get(service) or []
    return list


def Locate(service):
    try:
        return LocateAll(service)[0]
    except IndexError:
        return None

