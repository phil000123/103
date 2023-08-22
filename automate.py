import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            event_type = "directory created"
        else:
            event_type = "file created"
        print(f"{event_type}: {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            event_type = "directory modified"
        else:
            event_type = "file modified"
        print(f"{event_type}: {event.src_path}")

    def on_moved(self, event):
        if event.is_directory:
            event_type = "directory moved/renamed"
        else:
            event_type = "file moved/renamed"
        print(f"{event_type}: {event.src_path} -> {event.dest_path}")

    def on_deleted(self, event):
        if event.is_directory:
            event_type = "directory deleted"
        else:
            event_type = "file deleted"
        print(f"{event_type}: {event.src_path}")

# Set the path for the directory to track changes
from_dir = "<C:\Users\phil lin>"

if not os.path.exists(from_dir):
    print("The specified directory does not exist.")
    sys.exit(1)

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

print(f"Watching directory: {from_dir}")
print("Press any key to stop the observer.")

try:
    # Wait for a key press to stop the observer
    input()
except KeyboardInterrupt:
    pass

observer.stop()
observer.join()

print("Observer stopped.")
