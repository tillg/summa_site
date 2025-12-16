#!/usr/bin/env python3
"""
Development server for Summarum website with auto-rebuild on file changes.

This script:
- Watches for changes in content, templates, and config files
- Automatically rebuilds the site when changes are detected
- Serves the site on a local HTTP server
- Provides colored console output for better visibility
"""

import os
import sys
import time
import threading
import http.server
import socketserver
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Import the site generator
import generate_site

# Configuration
HOST = "localhost"
PORT = 8000
OUTPUT_DIR = "docs"
WATCH_PATHS = ["content", "templates", "static"]
WATCH_FILES = ["design_variables.py", "config.py", "generate_site.py"]

# ANSI color codes for terminal output
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    CYAN = '\033[96m'


class SiteRebuilder(FileSystemEventHandler):
    """Handles file system events and triggers site rebuild."""

    def __init__(self):
        super().__init__()
        self.last_rebuild = 0
        self.rebuild_delay = 1.0  # Debounce: wait 1 second before rebuilding
        self.rebuild_timer = None
        self.lock = threading.Lock()

    def should_process_event(self, event):
        """Check if the event should trigger a rebuild."""
        # Ignore directory events
        if event.is_directory:
            return False

        # Ignore hidden files and system files
        path = Path(event.src_path)
        if any(part.startswith('.') for part in path.parts):
            return False

        # Ignore output directory
        if OUTPUT_DIR in path.parts:
            return False

        # Only process relevant file types
        relevant_extensions = ['.md', '.html', '.py', '.css', '.js', '.svg', '.png', '.jpg']
        if path.suffix.lower() not in relevant_extensions:
            return False

        return True

    def schedule_rebuild(self, event):
        """Schedule a rebuild with debouncing."""
        if not self.should_process_event(event):
            return

        with self.lock:
            # Cancel any pending rebuild
            if self.rebuild_timer is not None:
                self.rebuild_timer.cancel()

            # Schedule a new rebuild
            self.rebuild_timer = threading.Timer(
                self.rebuild_delay,
                self.rebuild_site,
                args=[event.src_path]
            )
            self.rebuild_timer.start()

    def rebuild_site(self, changed_file):
        """Rebuild the site."""
        with self.lock:
            self.rebuild_timer = None

            # Check if enough time has passed since last rebuild
            current_time = time.time()
            if current_time - self.last_rebuild < self.rebuild_delay:
                return

            self.last_rebuild = current_time

            # Print rebuild notification
            timestamp = datetime.now().strftime("%H:%M:%S")
            rel_path = os.path.relpath(changed_file)

            print(f"\n{Colors.CYAN}[{timestamp}]{Colors.RESET} "
                  f"{Colors.YELLOW}Change detected:{Colors.RESET} {rel_path}")
            print(f"{Colors.BLUE}🔨 Rebuilding site...{Colors.RESET}")

            try:
                # Run the site generator
                generate_site.generate_site()
                print(f"{Colors.GREEN}✅ Rebuild complete!{Colors.RESET}\n")
            except Exception as e:
                print(f"{Colors.RED}❌ Rebuild failed: {e}{Colors.RESET}\n")

    def on_modified(self, event):
        """Called when a file is modified."""
        self.schedule_rebuild(event)

    def on_created(self, event):
        """Called when a file is created."""
        self.schedule_rebuild(event)

    def on_deleted(self, event):
        """Called when a file is deleted."""
        self.schedule_rebuild(event)


class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with minimal logging."""

    def log_message(self, format, *args):
        """Override to reduce verbosity."""
        # Only log errors
        if args[1] != '200':
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"{Colors.CYAN}[{timestamp}]{Colors.RESET} "
                  f"{Colors.RED}{self.address_string()} - {format % args}{Colors.RESET}")


def start_http_server():
    """Start the HTTP server in a separate thread."""
    os.chdir(OUTPUT_DIR)

    # Create server
    Handler = QuietHTTPRequestHandler
    with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
        print(f"{Colors.GREEN}📡 Server running at {Colors.BOLD}http://{HOST}:{PORT}/{Colors.RESET}")
        print(f"{Colors.CYAN}📂 Serving files from: {Colors.RESET}{os.getcwd()}\n")
        httpd.serve_forever()


def start_file_watcher():
    """Start watching for file changes."""
    event_handler = SiteRebuilder()
    observer = Observer()

    # Watch specified directories
    for path in WATCH_PATHS:
        if os.path.exists(path):
            observer.schedule(event_handler, path, recursive=True)
            print(f"{Colors.CYAN}👀 Watching:{Colors.RESET} {path}/")

    # Watch specified files
    for file in WATCH_FILES:
        if os.path.exists(file):
            observer.schedule(event_handler, file, recursive=False)
            print(f"{Colors.CYAN}👀 Watching:{Colors.RESET} {file}")

    observer.start()
    print()
    return observer


def main():
    """Main entry point for the development server."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}  Summarum Development Server{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}\n")

    # Initial build
    print(f"{Colors.BLUE}🚀 Performing initial build...{Colors.RESET}")
    try:
        generate_site.generate_site()
        print(f"{Colors.GREEN}✅ Initial build complete!{Colors.RESET}\n")
    except Exception as e:
        print(f"{Colors.RED}❌ Initial build failed: {e}{Colors.RESET}")
        print(f"{Colors.RED}Please fix the errors and try again.{Colors.RESET}\n")
        sys.exit(1)

    # Start file watcher
    observer = start_file_watcher()

    # Start HTTP server in a separate thread
    server_thread = threading.Thread(target=start_http_server, daemon=True)
    server_thread.start()

    # Instructions
    print(f"{Colors.YELLOW}💡 Tips:{Colors.RESET}")
    print(f"   • Edit files in content/, templates/, or config files")
    print(f"   • Site will automatically rebuild on changes")
    print(f"   • Refresh your browser to see updates")
    print(f"   • Press {Colors.BOLD}Ctrl+C{Colors.RESET} to stop\n")

    print(f"{Colors.GREEN}✨ Development server is ready!{Colors.RESET}")
    print(f"{Colors.CYAN}{'─'*60}{Colors.RESET}\n")

    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}🛑 Shutting down development server...{Colors.RESET}")
        observer.stop()
        observer.join()
        print(f"{Colors.GREEN}✅ Server stopped. Goodbye!{Colors.RESET}\n")


if __name__ == "__main__":
    main()
