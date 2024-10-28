import os
import datetime
import shutil
from PIL import Image
import pandas as pd
import PyPDF2

# 1. File Renamer
def rename_files(folder_path, prefix="file_", add_timestamp=False):
    for count, filename in enumerate(os.listdir(folder_path)):
        file_extension = os.path.splitext(filename)[1]
        if add_timestamp:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            new_name = f"{prefix}{timestamp}_{count}{file_extension}"
        else:
            new_name = f"{prefix}{count}{file_extension}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
    print("Files renamed successfully.")

# 2. File Organizer
def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_extension = os.path.splitext(filename)[1][1:]  # Remove the dot
        if file_extension:  # Skip files without an extension
            destination_folder = os.path.join(folder_path, file_extension.upper())
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(os.path.join(folder_path, filename), os.path.join(destination_folder, filename))
    print("Files organized by type successfully.")

# 3. Text Extraction from PDF
def extract_text_from_pdf(pdf_path, output_txt_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    with open(output_txt_path, "w") as txt_file:
        txt_file.write(text)
    print("Text extracted from PDF successfully.")

# 4. Image Converter
def convert_image_format(input_folder, output_folder, output_format="PNG"):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(os.path.join(input_folder, filename))
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img.save(output_path, output_format)
    print("Images converted successfully.")

# 5. CSV to Excel Converter
def csv_to_excel(csv_path, excel_path):
    df = pd.read_csv(csv_path)
    df.to_excel(excel_path, index=False)
    print("CSV file converted to Excel format successfully.")

# Example Usage
if __name__ == "__main__":
    # Rename files
    rename_files("path_to_folder", prefix="image_", add_timestamp=True)
    
    # Organize files by type
    organize_files("path_to_folder")
    
    # Extract text from a PDF
    extract_text_from_pdf("path_to_pdf.pdf", "output_text.txt")
    
    # Convert images to PNG format
    convert_image_format("path_to_input_images", "path_to_output_images", output_format="PNG")
    
    # Convert CSV to Excel
    csv_to_excel("path_to_input.csv", "output.xlsx")
