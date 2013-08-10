from ServiceLocator import locate_all,discover_services
from MIMERecognizers.MIMERecognizerService import MIMERecognizerService
from FileOpeners.FileOpenerService import FileOpenerService

discover_services(__file__)

file = "main.htm"
extension = file[-4:]

MIMERecognizers = locate_all(MIMERecognizerService)
mimes = [service.get_MIME_type() for service in MIMERecognizers
         if service.recognizes_extension(extension)]

FileOpeners = locate_all(FileOpenerService)
for service in FileOpeners:
    [service.open(file) for mime in mimes
     if service.can_open_mime_type(mime)]
