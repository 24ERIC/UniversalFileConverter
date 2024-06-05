import subprocess

def convert_epub_to_pdf(epub_file, pdf_file):
    try:
        # Check if Calibre's ebook-convert tool is available
        subprocess.run(['ebook-convert', '--version'], check=True)
        
        # Convert EPUB to PDF
        subprocess.run(['ebook-convert', epub_file, pdf_file], check=True)
        print(f"Successfully converted {epub_file} to {pdf_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("Calibre's ebook-convert tool not found. Please ensure Calibre is installed and available in your PATH.")

# Example usage
convert_epub_to_pdf('a.epub', 'a.pdf')
