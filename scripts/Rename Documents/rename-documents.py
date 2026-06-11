import os

# ===== USER CONFIGURATION =====
folder_path = r"C:\Users\\Path\To\Folder\Rename Documents"

prefix_name = "Name of File"
lang = "EN FR"
version = "Vx"
date_str = "DDMMMYYYY"
study_title = "AROMAPT-SC-1001"
# ==============================

# File types to process
valid_extensions = (".pdf", ".docx", ".xlsx", ".pptx")


# Loop through all files in directory
for filename in os.listdir(folder_path):
    if filename.lower().endswith(valid_extensions):
        
        original_name = os.path.splitext(filename)[0]
        extension = os.path.splitext(filename)[1]

        # Build new file name
        new_name = f"{prefix_name} ({lang}, {version}, {date_str})_{study_title}_{original_name}{extension}"
        
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        # Avoid overwriting existing files
        if os.path.exists(new_path):
            print(f"Skipping (already exists): {new_name}")
        else:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")