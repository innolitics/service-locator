from FileOpenerService import FileOpenerService
from ServiceLocator import ServiceProvider
from MIMERecognizers.MIMERecognizerService import MIMERecognizerService

#some classes can be multiple service providers
@ServiceProvider(FileOpenerService, MIMERecognizerService)
class WavOpener(FileOpenerService, MIMERecognizerService):
    def can_open_mime_type(self, mime):
        return mime == "audio/wav"

    def open(self, file):
        print "opening with audio wav editor"

    def recognizes_extension(self, extension):
        return extension == ".wav"

    def get_MIME_type(self):
        return "audio/wav"