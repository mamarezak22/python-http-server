from .handler import HTTPHandler
from .handlers import EchoHandler
from .response import HTTPResponse
from urllib.parse import urlparse,parse_qs

class Router:
    def __init__(self):
        self.routes = []


    def add_route(self,path, handler : HTTPHandler):
        normalized_path = path.strip("/").split("/")
        self.routes.append((normalized_path, handler))

    def _match(self,route_parts : list[str] , url_parts : list[str]) -> tuple[bool,dict[str,str]]:
        if len(route_parts) != len(url_parts):
            return False, {}

        params = {}
        for route , actual in zip(route_parts, url_parts):
            #the cases that a part of route is path parameter.
            if route.startswith(":"):
                params[route[1:]] = actual
            #the cases that a part of route is a literal and should match with the requested route.
            elif route != actual:
                return False, {} 
        return True, params 

    def _get_query_params(self,request) -> dict[str,str]:
        parsed_url = urlparse(request.url.raw_url)
        query_params = {k: v[0] for k, v in parse_qs(parsed_url.query).items()}
        return query_params

    def handle_request(self, request)->HTTPResponse:
        url_parts = request.url.raw_url.strip("/").split("/")
        request.url.query_params = self._get_query_params(request)

        for route_parts, handler in self.routes:
            matched, path_params = self._match(route_parts, url_parts)
            if matched:
                request.url.path_params = path_params
                return handler.handle(request)

        return HTTPResponse.not_found()

router = Router()

def register_routes() -> None:
    router.add_route( "/hello/:word", EchoHandler())