import os
import shutil

def copy_tutorial_md(source_dir, destination_dir):
    count = 0
    for folder in os.listdir(source_dir):
        subfolder_path = os.path.join(source_dir, folder)
        # print(subfolder_path)
        if os.path.isdir(subfolder_path) and os.path.exists(os.path.join(subfolder_path, ".tutorial")):
            # print(subfolder_path)
            tutorial_source_dir = os.path.join(subfolder_path, ".tutorial")
            # print(tutorial_source_dir)
            for filename in os.listdir(tutorial_source_dir):
                if filename.endswith(".md"):
                    count = count + 1
                    tutorial_source = os.path.join(tutorial_source_dir, filename)
                    tutorial_destination = os.path.join(destination_dir, f"{folder}_{filename}")
                    # print(f"count {count} and file name {filename} save at {tutorial_destination}")
                    
                    try:
                        shutil.copy2(tutorial_source, tutorial_destination)
                        print(f"Copied '{tutorial_source}' to '{tutorial_destination}'")
                    except OSError as e:
                        print(f"Error copying '{tutorial_source}': {e}")
                        break

source_dir = "/home/aayush/Downloads/Test/100-days-of-code-youtube"
destination_dir = "/media/HDD1/Courses/Python/Basics/Notes"
copy_tutorial_md(source_dir, destination_dir)