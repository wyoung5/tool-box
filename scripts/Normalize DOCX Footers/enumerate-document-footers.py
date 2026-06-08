# Import docx library to process files
from docx import Document

# Import glob to define file in directory
import glob

docx_files = glob.glob("*.docx")


if len(docx_files) == 0:
    raise FileNotFoundError("No .docx file found in the working directory.")
elif len(docx_files) > 1:
    raise ValueError(f"Multiple .docx files found: {docx_files}")

input_file = docx_files[0]
output_file = "output_normalized.docx"

doc = Document(input_file)

for i, section in enumerate(doc.sections):
    print(f"Section {i} footer text:")
    for para in section.footer.paragraphs:
        print("   ", para.text)