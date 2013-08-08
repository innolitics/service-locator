from FileOpenerService import FileOpenerService
from ServiceLocator import ServiceProvider


@ServiceProvider(FileOpenerService)
class HTMLOpener(FileOpenerService):

    def can_open_mime_type(self, mime):
        return mime == "text/html"

    def open(self, file):
        print "opening with google chrome"
