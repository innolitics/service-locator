from servicelocator.lookup import service_provider
from tests.integration.FileOpeners.FileOpenerService import FileOpenerService


@service_provider(FileOpenerService)
class PDFOpener(FileOpenerService):

    def can_open_mime_type(self, mime):
        return mime == "application/pdf"

    def open(self, file):
        print("opening with adobe reader")
