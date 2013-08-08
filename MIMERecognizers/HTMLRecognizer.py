from MIMERecognizerService import MIMERecognizerService
from ServiceLocator import ServiceProvider


@ServiceProvider(MIMERecognizerService)
class HTMLRecognizer(MIMERecognizerService):
    def recognizes_extension(self, extension):
        return extension == ".html" or extension == ".htm"

    def get_MIME_type(self):
        return "text/html"
