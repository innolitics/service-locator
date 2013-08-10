from ..MIMERecognizerService import MIMERecognizerService
from ServiceLocator import ServiceProvider


@ServiceProvider(MIMERecognizerService)
class MP3Recognizer(MIMERecognizerService):
    def recognizes_extension(self, extension):
        return extension == ".mp3"

    def get_MIME_type(self):
        return "audio/x-mp3"
