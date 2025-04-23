import asyncio
from http.server import main
import app.routes #to routes be registered

if __name__ == "__main__":
    asyncio.run(main())

