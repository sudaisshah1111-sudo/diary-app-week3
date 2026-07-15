# Diary App — Week 3 (File I/O & Exception Handling)

A command-line personal diary application built with Python, demonstrating file handling, JSON storage, CSV export, and custom exception handling.

## Features
- Add diary entries with date and text
- View all saved entries
- Delete entries by number
- Export all entries to a CSV file
- Handles missing or corrupted data files gracefully
- Custom exception (`DiaryError`) for invalid delete operations

## Concepts Used
- File I/O (`open()`, read/write modes)
- JSON serialization (`json.load`, `json.dump`)
- CSV export (`csv.DictWriter`)
- Exception handling (`try` / `except` / `finally`)
- Custom exception classes

## Installation

1. Make sure Python 3 is installed on your system.
2. Clone this repository: