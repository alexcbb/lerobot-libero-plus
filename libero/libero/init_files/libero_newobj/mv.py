import os
import shutil

def filter_and_copy_bddl():
    # Configuration
    source_folders = ["libero_spatial", "libero_object", "libero_10", "libero_goal"]
    destination_folder = "libero_distractors"

    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
            print(f"Created directory: {destination_folder}")
        except OSError as e:
            print(f"Error creating directory: {e}")
            return

    files_copied = 0
    
    for source_folder in source_folders:
        if not os.path.exists(source_folder):
            print(f"Error: Source folder '{source_folder}' not found in the current directory.")
            continue

        print(f"Scanning '{source_folder}' for .bddl files containing '_add' with id 1-10...")

        for filename in os.listdir(source_folder):
            if filename.endswith(".pruned_init"):
                # Check if filename ends with _add_{id}.bddl for id 1 to 10
                is_target = False
                for i in range(1, 11):
                    if filename.endswith(f"_add_{i}.pruned_init"):
                        is_target = True
                        break
                
                if is_target:
                    source_path = os.path.join(source_folder, filename)
                    try:
                        dest_path = os.path.join(destination_folder, filename)
                        shutil.copy2(source_path, dest_path)
                        print(f" -> Copied: {filename}")
                        files_copied += 1
                    except Exception as e:
                        print(f"Could not process {filename}: {e}")

    print("-" * 30)
    print(f"Process complete. Total files copied: {files_copied}")

if __name__ == "__main__":
    filter_and_copy_bddl()
