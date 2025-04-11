from .request import HTTPRequest
from .response import HTTPResponse
from abc import ABC


#a handler to be inherate from and implement the methods user want on that url.
class HTTPHandler(ABC):
    def get(self,request:HTTPRequest)->HTTPResponse:
        return HTTPResponse.method_not_allowed()
    def post(self,request: HTTPRequest)->HTTPResponse:
        return HTTPResponse.method_not_allowed()
    def put(self,request: HTTPRequest)->HTTPResponse:
        return HTTPResponse.method_not_allowed()
    def delete(self,request: HTTPRequest)->HTTPResponse:
        return HTTPResponse.method_not_allowed()
    def patch(self,request: HTTPRequest)->HTTPResponse:
        return HTTPResponse.method_not_allowed()
    def handle(self,request:HTTPRequest)->HTTPResponse:
        method = request.method.lower()
        handler = getattr(self, method, None)
        base_handler = getattr(HTTPHandler, method, None)

        # if method is overridden in subclass, use it
        if handler and handler.__func__ is not base_handler:
            return handler(request)

        return HTTPResponse.method_not_allowed()  
        

        