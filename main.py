from lookup import global_lookup
from service_discoverer import discover_services
from MIMERecognizers.MIMERecognizerService import MIMERecognizerService
from FileOpeners.FileOpenerService import FileOpenerService

discover_services(__file__)

file = "main.htm"
extension = file[-4:]

MIMERecognizers = global_lookup.lookup_all(MIMERecognizerService)
mimes = [service.get_MIME_type() for service in MIMERecognizers
         if service.recognizes_extension(extension)]

FileOpeners = global_lookup.lookup_all(FileOpenerService)
for service in FileOpeners:
    [service.open(file) for mime in mimes
     if service.can_open_mime_type(mime)]
