import sys
import os
import asyncio
import uvicorn

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.server.server import server

def main():
    print('Starting LLM server...')
    try:
        # Start the web server
        uvicorn.run(server, host="0.0.0.0", port=1307)

    except KeyboardInterrupt:
        pass
        # listener.stop_listening()


if __name__ == "__main__":
    main()