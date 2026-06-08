import os
from PyPDF2 import PdfMerger

def combine_pdfs(input_folder, output_file):
    # Get all PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

    # Sort files alphabetically
    pdf_files.sort()

    # Create a PdfMerger object
    merger = PdfMerger()

    # Append each PDF to the merger
    for pdf_file in pdf_files:
        file_path = os.path.join(input_folder, pdf_file)
        merger.append(file_path)

    # Write the merged PDF to the output file
    merger.write(output_file)
    merger.close()

    print(f"Successfully combined {len(pdf_files)} PDFs into {output_file}")

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Set input folder (current directory) and output file
    input_folder = script_dir
    output_file = os.path.join(script_dir, "combined_output.pdf")

    # Run the combination
    combine_pdfs(input_folder, output_file)
