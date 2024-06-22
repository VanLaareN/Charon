import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, directory_to_watch):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            # Event is created, you can process it now
            print(f"Received created event - {event.src_path}")
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print(f"Received modified event - {event.src_path}")
        elif event.event_type == 'deleted':
            # Event is deleted, you can process it now
            print(f"Received deleted event - {event.src_path}")

if __name__ == '__main__':
    path = "/home/karlo/Documents/Charon"
    watcher = Watcher(path)
    watcher.run()
