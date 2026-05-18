import os

# Your Godot project folder
PROJECT_FOLDER = r"D:\Game developing\Echoes-of-the-prophecy-surviver"

# Output file
OUTPUT_FILE = "all_gdscript.txt"

# Folders to ignore
IGNORE_FOLDERS = {
    ".godot",
    "addons",
    "cache",
    ".import"
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    # Walk through every folder/subfolder
    for root, dirs, files in os.walk(PROJECT_FOLDER):

        # Skip ignored folders
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        for file in files:

            # Only read .gd files
            if file.endswith(".gd"):

                file_path = os.path.join(root, file)

                try:
                    # Read script content
                    with open(file_path, "r", encoding="utf-8") as gd_file:
                        content = gd_file.read()

                    # Write filename on top
                    output.write(f"{file}:\n")

                    # Write script content
                    output.write(content)

                    # Add spacing between scripts
                    output.write("\n\n")

                    print(f"Added: {file_path}")

                except Exception as e:
                    print(f"Failed to read {file_path}: {e}")

print("Done.")