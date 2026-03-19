import shutil
from pathlib import Path

def organize_files():
    # Define target using Path object
    download_dir = Path("/sdcard/Download")
    
    if not download_dir.exists():
        print("Error: Target directory not found.")
        return

    # Map extensions to destination folder names
    categories = {
        ".pdf": "PDF_Documents",
        ".py": "Python_Scripts",
        ".txt": "Text_Files"
    }

    print("Starting organization...\n")
    moved_count = 0

    # iterdir() goes through everything in the folder
    for item in download_dir.iterdir():
        # We only want to move actual files, not folders
        if item.is_file():
            ext = item.suffix.lower()
            
            # If the extension is in our dictionary, we organize it
            if ext in categories:
                dest_folder_name = categories[ext]
                dest_path = download_dir / dest_folder_name
                
                # Create the category folder if it doesn't exist yet
                dest_path.mkdir(exist_ok=True)
                
                # The exact path where the file will live
                target_file = dest_path / item.name
                
                # Check if file already exists there to prevent data loss
                if not target_file.exists():
                    # Move the file
                    shutil.move(str(item), str(target_file))
                    print(f"Moved: {item.name} -> {dest_folder_name}/")
                    moved_count += 1
                else:
                    print(f"Skipped: {item.name} (Already exists in {dest_folder_name}/)")

    print(f"\nFinal Version Complete. Successfully moved {moved_count} files.")

if __name__ == "__main__":
    organize_files()