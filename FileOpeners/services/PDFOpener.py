from ..FileOpenerService import FileOpenerService
from ServiceLocator import ServiceProvider


@ServiceProvider(FileOpenerService)
class PDFOpener(FileOpenerService):

    def can_open_mime_type(self, mime):
        return mime == "application/pdf"

    def open(self, file):
        print("opening with adobe reader")
