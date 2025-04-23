
supported_methods = ["GET","POST","PUT","DELETE","PATCH"]

class HTTPRequest:
    def __init__(self,url : str , method : str , headers : dict[str,str] = {} , body : str  = "",http_version : str = "HTTP/1.1"):
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body
        self.http_version = http_version
        self.query_params : dict[str,str] = {}
        self.path_params : dict[str,str] = {}



def parse_request_msg(request_msg : bytes)->HTTPRequest:
    request_lines = request_msg.decode().split("\r\n")
    method , url , http_version = request_lines[0].split(" ")
    if method not in supported_methods:
        raise ValueError(f"Unsupported method {method}")
    headers = {}
    for line in request_lines[1:]:
        if line == "":
            break
        key , value = line.split(": ",1)
        headers[key] = value
    body = request_lines[len(headers)+2:][0]

    return HTTPRequest(url, method, headers, body, http_version)