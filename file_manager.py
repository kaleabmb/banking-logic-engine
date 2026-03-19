import os

# First try: Basic OS module file counter
def count_files():
    # Android default download path
    target_dir = "/sdcard/Download"
    
    # Check if directory exists to prevent crashes
    if not os.path.exists(target_dir):
        print(f"Error: Directory {target_dir} not found.")
        return

    print(f"Scanning directory: {target_dir}...\n")

    pdf_count = 0
    py_count = 0
    txt_count = 0
    other_count = 0

    # Get all files and folders in the target directory
    items = os.listdir(target_dir)

    for item in items:
        # Ignore folders, only process files
        if os.path.isfile(os.path.join(target_dir, item)):
            item_lower = item.lower()
            if item_lower.endswith(".pdf"):
                pdf_count += 1
            elif item_lower.endswith(".py"):
                py_count += 1
            elif item_lower.endswith(".txt"):
                txt_count += 1
            else:
                other_count += 1

    print("--- File Tally ---")
    print(f"PDF files: {pdf_count}")
    print(f"Python files: {py_count}")
    print(f"Text files: {txt_count}")
    print(f"Other files: {other_count}")

if __name__ == "__main__":
    count_files()