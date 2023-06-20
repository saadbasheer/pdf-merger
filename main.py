import PyPDF2 as pdf
import os

inputdir = r'C:\Users\saadbasheer\Desktop\Code\Python\Projects\pdfmerger\input'
outputdir = r'C:\Users\saadbasheer\Desktop\Code\Python\Projects\pdfmerger\output'

def pdfmerger(input_dir, output_dir):
    merger = pdf.PdfMerger()
    filename = "merged_pdf"
    for files in os.listdir(inputdir):
        if files.endswith('.pdf'):
            merger.append(os.path.join(inputdir, files))

    merger.write(os.path.join(output_dir, filename))


pdfmerger(inputdir, outputdir)
