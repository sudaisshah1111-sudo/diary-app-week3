import json
import csv


class DiaryError(Exception):
    pass


def load_entries(filename="diary_data.json"):
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
    with open(filename, "w") as f:
        json.dump(entries, f, indent=2)


def add_entry(entries):
    text = input("Write your diary entry: ")
    entries.append({"date": "2026-07-14", "entry": text})
    print("Entry saved!")


def view_entries(entries):
    if not entries:
        print("No entries yet.")
        return
    for i, e in enumerate(entries, 1):
        print(f"{i}. [{e['date']}] {e['entry']}")


def delete_entry(entries, index):
    try:
        removed = entries.pop(index - 1)
        print(f"Deleted: {removed['entry']}")
    except IndexError:
        raise DiaryError(f"No entry numbered {index}. You have {len(entries)} entries.")
    finally:
        print("Delete attempt finished.")


def export_csv(entries, filename="diary_export.csv"):
    if not entries:
        print("No entries to export.")
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "entry"])
        writer.writeheader()
        for e in entries:
            writer.writerow(e)
    print(f"Exported to {filename}")


def main():
    entries = load_entries()
    while True:
        print("\n--- Diary Menu ---")
        print("1. Add entry")
        print("2. View entries")
        print("3. Delete entry")
        print("4. Export to CSV")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry(entries)
            save_entries(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            try:
                idx = int(input("Enter entry number to delete: "))
                delete_entry(entries, idx)
                save_entries(entries)
            except ValueError:
                print("Please type a valid number.")
            except DiaryError as e:
                print("Error:", e)
        elif choice == "4":
            export_csv(entries)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()