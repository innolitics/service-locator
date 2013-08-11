from servicelocator.lookup import service_provider
from tests.integration.FileOpeners.FileOpenerService import FileOpenerService


@service_provider(FileOpenerService)
class HTMLOpener(FileOpenerService):

    def can_open_mime_type(self, mime):
        return mime == "text/html"

    def open(self, file):
        print("opening with google chrome")
