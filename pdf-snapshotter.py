from pdf2image import convert_from_path
import os

def pdf_first_page_to_png(pdf_file, output_file):
    try:
        images = convert_from_path(pdf_file, first_page=1, last_page=1)
        for image in images:
            image.save(output_file, 'PNG')
    except Exception as e:
        print(f"Error converting file {pdf_file}: {e}")

def format_output_filename(folder_name, file_name, naming_format):
    file_base_name = os.path.splitext(file_name)[0]
    folder_parts = folder_name.split()
    file_parts = file_name.split()

    output_filename = naming_format.replace('%foldername%', folder_name)
    output_filename = output_filename.replace('%filename%', file_base_name)
    output_filename = output_filename.replace('%folderpart1%', folder_parts[0] if len(folder_parts) > 0 else '')
    output_filename = output_filename.replace('%folderpart2%', folder_parts[1] if len(folder_parts) > 1 else '')
    output_filename = output_filename.replace('%filepart1%', file_parts[0] if len(file_parts) > 0 else '')

    return f"{output_filename}.png"

def main():
    print("Welcome to PDF SnapShotter!")

    # User input for directories
    print("\nEnter the relative path of the root directory containing the PDFs.")
    print("Example: ./Exam Folder")
    root_directory = input("Root directory path: ")

    print("\nEnter the full path of the output directory where PNGs will be saved.")
    print("Example: ./")
    output_directory = input("Output directory path: ")

    # Naming format options
    print("\nChoose a naming format for the output files:")
    print("1. Folder name followed by file name (Example: Folder_Filename.png)")
    print("2. First word of folder name followed by first word of file name (Example: Folderpart1_Filepart1.png)")
    print("3. Custom format using placeholders")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "2":
        naming_format = "%folderpart1%_%filepart1%"
    elif choice == "3":
        print("\nFor custom format, use the following placeholders:")
        print("%foldername% - Full name of the folder")
        print("%filename% - Base name of the file (without extension)")
        print("%folderpart1% - First word of the folder name")
        print("%folderpart2% - Second word of the folder name")
        print("%filepart1% - First word of the file name")
        print("Example: %folderpart1%_%filename%_snapshot")
        naming_format = input("Enter your custom format: ")
    else:
        naming_format = "%foldername%_%filename%"

    # Processing PDFs
    for subdir, dirs, files in os.walk(root_directory):
        folder_name = os.path.basename(subdir)
        for filename in files:
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(subdir, filename)
                output_filename = format_output_filename(folder_name, filename, naming_format)
                output_path = os.path.join(output_directory, output_filename)
                pdf_first_page_to_png(pdf_path, output_path)
                print(f"Converted {pdf_path} to {output_path}")

if __name__ == "__main__":
    main()