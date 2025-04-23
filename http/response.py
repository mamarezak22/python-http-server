
map_status_code_to_text: dict[int, str] = {
    100: "Continue",
    101: "Switching Protocols",
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
}


class HTTPResponse:
    def __init__(self,status_code , headers : dict[str,str] = {}, body : str = "",http_version : str = "HTTP/1.1"):
        self.status_code = status_code
        self.status_text = map_status_code_to_text[status_code]
        self.headers = headers
        self.body = body
        self.http_version = http_version


    @property
    def message(self)->str:
        status_line = f"{self.http_version} {self.status_code} {self.status_text}\r\n"
        headers = "".join(f"{k}: {v}\r\n" for k, v in self.headers.items())
        body = f"\r\n{self.body}" if self.body else "\r\n"
        message = status_line + headers + body
        return message

    @classmethod
    def method_not_allowed(cls):
        return cls(status_code = 405)
    
    @classmethod
    def not_found(cls):
        return cls(status_code = 404)
