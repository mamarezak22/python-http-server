from .handler import HTTPHandler
from .response import HTTPResponse

class EchoHandler(HTTPHandler):
    def get(self, request):
        word = request.url.path_params.get('word')
        return HTTPResponse( 
            status_code=200,
            body=f"Echo: {word}"
        )