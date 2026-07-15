"""
Diary App - Week 3 Project
A command-line personal diary application demonstrating:
- File I/O (reading and writing files)
- JSON data storage
- CSV export
- Custom exception handling with try/except/finally

Author: Sudais Shah
"""

import json
import csv
from datetime import date


class DiaryError(Exception):
    """Custom exception raised for diary-specific errors,
    such as trying to delete or edit an entry that doesn't exist."""
    pass


def load_entries(filename="diary_data.json"):
    """
    Load diary entries from a JSON file.
    Returns an empty list if the file doesn't exist or is corrupted,
    instead of crashing the program.
    """
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No diary file found yet — starting fresh.")
        return []
    except json.JSONDecodeError:
        print("Diary file is corrupted — starting a new one.")
        return []


def save_entries(entries, filename="diary_data.json"):
    """Save the current list of diary entries to a JSON file."""
    with open(filename, "w") as f:
        json.dump(entries, f, indent=2)


def add_entry(entries):
    """Prompt the user for a new diary entry and append it to the list."""
    text = input("Write your diary entry: ")
    entries.append({"date": str(date.today()), "entry": text})
    print("Entry saved!")


def view_entries(entries):
    """Print all diary entries, numbered, with their date."""
    if not entries:
        print("No entries yet.")
        return
    for i, e in enumerate(entries, 1):
        print(f"{i}. [{e['date']}] {e['entry']}")


def edit_entry(entries, index):
    """
    Edit the text of an existing entry by its displayed number (1-based).
    Raises DiaryError if the number doesn't exist.
    """
    try:
        entry = entries[index - 1]
        print(f"Current text: {entry['entry']}")
        new_text = input("Enter new text: ")
        entry["entry"] = new_text
        print("Entry updated!")
    except IndexError:
        raise DiaryError(f"No entry numbered {index}. You have {len(entries)} entries.")


def delete_entry(entries, index):
    """
    Delete an entry by its displayed number (1-based).
    Raises DiaryError if the number doesn't exist.
    The finally block always runs, confirming the attempt is complete.
    """
    try:
        removed = entries.pop(index - 1)
        print(f"Deleted: {removed['entry']}")
    except IndexError:
        raise DiaryError(f"No entry numbered {index}. You have {len(entries)} entries.")
    finally:
        print("Delete attempt finished.")


def search_entries(entries, keyword):
    """Print all entries whose text contains the given keyword (case-insensitive)."""
    matches = [e for e in entries if keyword.lower() in e["entry"].lower()]
    if not matches:
        print(f"No entries found containing '{keyword}'.")
        return
    print(f"Found {len(matches)} matching entr{'y' if len(matches) == 1 else 'ies'}:")
    for e in matches:
        print(f"[{e['date']}] {e['entry']}")


def export_csv(entries, filename="diary_export.csv"):
    """Export all diary entries to a CSV file with 'date' and 'entry' columns."""
    if not entries:
        print("No entries to export.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "entry"])
        writer.writeheader()
        for e in entries:
            writer.writerow(e)
    print(f"Exported to {filename}")


def print_menu():
    """Display the main menu options."""
    print("\n--- Diary Menu ---")
    print("1. Add entry")
    print("2. View entries")
    print("3. Edit entry")
    print("4. Delete entry")
    print("5. Search entries")
    print("6. Export to CSV")
    print("7. Exit")


def main():
    """Main program loop: load data, show menu, handle user choices."""
    entries = load_entries()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry(entries)
            save_entries(entries)

        elif choice == "2":
            view_entries(entries)

        elif choice == "3":
            try:
                idx = int(input("Enter entry number to edit: "))
                edit_entry(entries, idx)
                save_entries(entries)
            except ValueError:
                print("Please type a valid number.")
            except DiaryError as e:
                print("Error:", e)

        elif choice == "4":
            try:
                idx = int(input("Enter entry number to delete: "))
                delete_entry(entries, idx)
                save_entries(entries)
            except ValueError:
                print("Please type a valid number.")
            except DiaryError as e:
                print("Error:", e)

        elif choice == "5":
            keyword = input("Enter keyword to search: ")
            search_entries(entries, keyword)

        elif choice == "6":
            export_csv(entries)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()