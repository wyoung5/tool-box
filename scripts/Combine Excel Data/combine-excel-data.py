import pandas as pd

# Input and output file paths
input_file = r"C:\Users\Path\To\File\input.xlsx"   # replace with your file
output_file = r"C:\Users\Path\To\File\output.xlsx"

# Define the expected columns (case-sensitive match in source sheets)
required_columns = [
    "Report Number",
    "Event",
    "Initial/FU",
    "Event Date",
    "Report Date"
]

# Final column order in output
final_columns = [
    "Project",
    "Report Number",
    "Event",
    "Initial/FU",
    "Event Date",
    "Report Date"
]

# Read all sheets
all_sheets = pd.read_excel(input_file, sheet_name=None)

# List to store processed data
combined_data = []

# Process each sheet
for sheet_name, df in all_sheets.items():
    # Make a copy to avoid modifying original
    df_copy = df.copy()

    # Check if required columns exist
    missing = [col for col in required_columns if col not in df_copy.columns]
    if missing:
        print(f"Skipping sheet '{sheet_name}' due to missing columns: {missing}")
        continue

    # Select required columns
    df_selected = df_copy[required_columns].copy()

    # Add Project column with sheet name
    df_selected["Project"] = sheet_name

    # Reorder columns
    df_selected = df_selected[final_columns]

    # Append to list
    combined_data.append(df_selected)

# Combine all sheets into one DataFrame
if combined_data:
    final_df = pd.concat(combined_data, ignore_index=True)

    # Write to new Excel file
    final_df.to_excel(output_file, index=False)

    print(f"✅ Data successfully consolidated into '{output_file}'")
else:
    print("❌ No valid sheets found to process.")
    input("Press Enter to exit...")

