#!/usr/bin/env python
import http.server
import queue
import sys
import threading
from pathlib import Path
from queue import SimpleQueue

import sphinx.cmd.build
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class QueuingEventHandler(FileSystemEventHandler):
    def __init__(self, q: SimpleQueue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._queue = q

    def on_any_event(self, event) -> None:
        self._queue.put_nowait(event)


class CustomDirHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='build/dirhtml', **kwargs)

    def log_error(self, format: str, *args) -> None:
        super().log_message(format, *args)

    def log_message(self, format: str, *args) -> None:
        pass


class HttpServerThread(threading.Thread):
    def __init__(self):
        super().__init__(name="HttpServer")
        self.server = http.server.ThreadingHTTPServer(('', 8999), CustomDirHandler)

    def run(self):
        (addr, port) = self.server.server_address
        print(f"Serving docs at http://{addr}:{port}/")
        self.server.serve_forever()


def main():
    rebuild()
    server_thread = HttpServerThread()
    server_thread.start()
    path = Path("./source")
    my_queue = SimpleQueue()
    handler = QueuingEventHandler(my_queue)

    observer = Observer()
    observer.schedule(handler, str(path), recursive=True)
    observer.start()
    print(f"Watching {path} for changes...", file=sys.stderr)
    try:
        while observer.is_alive():
            try:
                my_queue.get(timeout=0.5)
            except queue.Empty:
                # Loop and check observer is alive
                continue
            while True:
                # debounce by waiting for next event
                try:
                    my_queue.get(timeout=0.5)
                except queue.Empty:
                    # there was none, break
                    break
            rebuild()
    finally:
        server_thread.server.shutdown()
        server_thread.join()
        observer.stop()
        observer.join()


def rebuild():
    print("Performing docs build", file=sys.stderr)
    target = 'dirhtml'
    exit_code = sphinx.cmd.build.main(['-b', target, 'source', 'build/' + target])
    if exit_code != 0:
        print("Sphinx exited with error code", exit_code, file=sys.stderr)


if __name__ == "__main__":
    main()
