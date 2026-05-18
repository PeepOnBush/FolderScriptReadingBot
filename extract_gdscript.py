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
I = 0
with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    # Walk through folders
    for root, dirs, files in os.walk(PROJECT_FOLDER):
        i = 0
        # Remove ignored folders from traversal
        dirs[:] = [d for d in dirs if d not in IGNORE_FOLDERS]

        for file in files:
            # Only .gd files
            if file.endswith(".gd"):
                I += 1
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as gd_file:
                        content = gd_file.read()

                    # Write file path + content
                    output.write(f"\n===== {file_path} =====\n")
                    output.write(content)
                    output.write("\n\n")

                    print(f"Added: {file_path}")
                 
                except Exception as e:
                    print(f"Failed to read {file_path}: {e}")
print(f"Total .gd files extracted: {I}")
print("Done.")