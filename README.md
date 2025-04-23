# python HTTP server

A simple HTTP server built using pure Python with support for custom route handlers and path/query parameters. Inspired by web frameworks but designed to be lightweight and educational.

---

## Features

- Async server using `asyncio`
- Routing with path and query parameter support
- Pluggable HTTP method handlers via subclassing
- Clean separation of request, response, and routing logic

---

## Usage

1. Clone this repo or copy the structure.
2. Create an `app/` directory and define your routes and handlers there.

```python
from http.handler import HTTPHandler
from http.response import HTTPResponse
from http.router import router

class EchoHandler(HTTPHandler):
    def get(self, request):
        word = request.path_params.get("word", "nothing")
        return HTTPResponse(
            status_code=200,
            body=f"Echo: {word}"
        )

# Register route
router.add_route("/echo/:word", EchoHandler())
```
3. Run the server using:

```bash
python -m http.server
```
