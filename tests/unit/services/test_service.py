from servicelocator.lookup import service_provider


class AbstractService(object):
    def i_am_a_service(self):
        pass


@service_provider(AbstractService)
class ConcreteService(AbstractService):
    def i_am_a_service(self):
        return True
