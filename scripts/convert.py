import os
import cairosvg
from pypdf import PdfReader, PdfWriter
from tqdm import tqdm
import shutil

# List of directories from 'lab1' to 'lab9'
directories = ['lab1', 'lab2', 'lab3', 'lab4', 'lab5', 'lab6', 'lab7', 'lab8', 'lab9']

for directory in tqdm(directories):
    # Output PDF file
    output_pdf_file = f"{directory}/{directory}_lab.pdf"
    output_lab_file = f"fullLabs/{directory}.pdf"
    
    # Initialize a PDF file writer
    pdf_writer = PdfWriter()

    # List all SVG files in the input directory
    svg_files = [f for f in os.listdir(directory) if f.endswith(".svg")]

    # Convert each SVG file to PDF and add to the PDF writer
    for svg_file in svg_files:
        # Input SVG file path
        svg_path = os.path.join(directory, svg_file)

        # Output PDF file path (temporary)
        pdf_file = os.path.splitext(svg_file)[0] + ".pdf"
        pdf_path = os.path.join(directory, pdf_file)

        try:
            # Convert SVG to PDF using cairosvg
            cairosvg.svg2pdf(url=svg_path, write_to=pdf_path)

            # Add the PDF page to the PDF writer
            pdf_reader = PdfReader(open(pdf_path, 'rb'))
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # Remove the temporary PDF file
            os.remove(pdf_path)
        except Exception as e:
            print(f"Error adding {svg_path} to the PDF: {e}")

    # Save the final PDF file
    with open(output_pdf_file, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    shutil.move(output_pdf_file, output_lab_file)
    
    
    # print(f"PDF file '{output_pdf_file}' created successfully.")
