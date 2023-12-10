# PDF SnapShotter

PDF SnapShotter is a Python script that converts the first page of PDF files into PNG images. It's designed to process multiple PDFs in a specified directory and offers flexible naming conventions for the output images.

## Features

- Batch convert the first page of PDFs to PNG images.
- Customizable output naming conventions.
- Ability to process PDFs in subdirectories.
- Interactive user interface for easy setup and operation.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- The `pdf2image` Python library installed. This can be installed via pip:
  ```
  pip install pdf2image
  ```
- The `poppler` utility should also be installed on your system, which can be installed with homebrew or others tools:
    - On macOS:
    ```
    brew install poppler
    ```
    - On Linux:
    ```
    sudo apt-get install poppler-utils
    ```

## Installation

To use PDF SnapShotter, follow these steps:

1. Clone or download this repository to your local machine.
2. Install the required Python library (pdf2image) if you haven't already.
3. Ensure poppler is installed and correctly set up in your system's PATH.

## Usage

To use PDF SnapShotter, run the script from your terminal:

```
python pdf_snapshotter.py
```

Follow the on-screen prompts to enter the root directory containing your PDFs, the output directory for the PNGs, and your choice of naming convention for the output files.

## Naming Conventions

You can choose from the following naming conventions or create a custom one using placeholders:

- **Folder name followed by file name**: Output files will be named after their respective folder and file names.
- **First word of folder name followed by first word of file name**: Output files will use the first word of the folder and file names.
- **Custom Format**: Create a custom naming format using placeholders like `%foldername%`, `%filename%`, `%folderpart1%`, etc.
