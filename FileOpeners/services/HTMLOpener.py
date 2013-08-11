from ..FileOpenerService import FileOpenerService
from lookup import ServiceProvider


@ServiceProvider(FileOpenerService)
class HTMLOpener(FileOpenerService):

    def can_open_mime_type(self, mime):
        return mime == "text/html"

    def open(self, file):
        print("opening with google chrome")
