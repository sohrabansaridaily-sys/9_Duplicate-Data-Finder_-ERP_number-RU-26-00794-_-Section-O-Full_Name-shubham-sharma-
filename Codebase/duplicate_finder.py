# Duplicate Data Finder (PS No. 9)

def process_duplicates(filename, ignore_case=False):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            raw_lines = file.readlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please enter a valid file name.")
        return

    # Clean newline characters (and extra spaces if ignore_case is True)
    entries = []
    for line in raw_lines:
        cleaned = line.strip() if ignore_case else line.rstrip("\r\n")
        if cleaned != "":
            entries.append(cleaned)

    if len(entries) == 0:
        print("File is empty. Nothing to check.")
        return

    # Prepare comparison list (lowercase if option 2 is chosen)
    compare_list = [item.lower() for item in entries] if ignore_case else entries

    # Use a set to find unique entries while preserving first-seen order
    unique_set = set()
    unique_ordered = []
    for item in compare_list:
        if item not in unique_set:
            unique_set.add(item)
            unique_ordered.append(item)

    total_items = len(compare_list)
    unique_count = len(unique_set)

    # Loop to count how many times each entry repeats
    duplicates = []
    for item in unique_ordered:
        count = 0
        for entry in compare_list:
            if entry == item:
                count += 1
        if count > 1:
            duplicates.append(f"{item} ({count} times)")

    # Print exact expected output
    print(f"\nTotal items: {total_items} | Unique items: {unique_count}")

    if len(duplicates) == 0:
        print("No duplicates found.")
    else:
        print("Duplicates: " + " | ".join(duplicates))
        with open("unique.txt", "w", encoding="utf-8") as out_file:
            for item in unique_ordered:
                out_file.write(item + "\n")
        print("Unique list saved to unique.txt\n")


def main():
    while True:
        print("\n=== DUPLICATE DATA FINDER ===")
        print("1. Find Duplicates (Exact match)")
        print("2. Find Duplicates (Ignore case & extra spaces)")
        print("3. Exit")

        choice = input("Select menu option (1-3): ").strip()

        if choice == "1":
            filename = input("Enter file name (e.g., data.txt): ").strip()
            process_duplicates(filename, ignore_case=False)
        elif choice == "2":
            filename = input("Enter file name (e.g., data.txt): ").strip()
            process_duplicates(filename, ignore_case=True)
        elif choice == "3":
            print("Exiting Duplicate Data Finder.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
  
