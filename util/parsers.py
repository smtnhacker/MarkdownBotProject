import subprocess
import io, os, tempfile

from pdf2image import convert_from_path

from util.image import pil2jpg

def md2pdf(content):

    pdf_binary = b''

    # Create temporary files
    fd_md, path_md = tempfile.mkstemp(suffix='.md')

    try:
        with os.fdopen(fd_md, 'w') as md_file:
            md_file.write(content)

        fd_pdf, path_pdf = tempfile.mkstemp(suffix='.pdf')

        print(f'Attempting to create pdf file {path_pdf}')

        try:
            subprocess.check_call(f"pandoc {path_md} -f markdown -t pdf -s -o {path_pdf}", shell=True)
            print('Successfully created pdf file!')

            with os.fdopen(fd_pdf, 'rb') as pdf_file:
                pdf_binary = pdf_file.read()
        finally:
            os.remove(path_pdf)

    finally:
        os.remove(path_md)

    return pdf_binary

def pdf2img(binary):

    fd_pdf, path_pdf = tempfile.mkstemp(suffix='.pdf')

    try:
        with os.fdopen(fd_pdf, 'wb') as pdf_file:
            pdf_file.write(binary)

        pages = convert_from_path(path_pdf, 500, fmt='jpeg')
        for idx, page in enumerate(pages):
            yield idx, pil2jpg(page)
            
    finally:
        os.remove(path_pdf)

def md2html(content):

    html_code = ''

    fd_md, path_md = tempfile.mkstemp(suffix='.md')
    fd_ht, path_ht = tempfile.mkstemp(suffix='.html')

    try:
        with os.fdopen(fd_md, 'w') as md_file:
            md_file.write(content)

        subprocess.check_call(f"pandoc {path_md} -f markdown -t html -s -o {path_ht} --webtex=https://latex.codecogs.com/svg.latex?", shell=True)

        with os.fdopen(fd_ht, 'r') as html_file:
            html_code = html_file.read()
    finally:
        os.remove(path_md)
        os.remove(path_ht)

    return html_code

def html2pdf(html_code):

    pdf_binary = b''

    fd_ht, path_ht = tempfile.mkstemp(suffix='.html')
    fd_pdf, path_pdf = tempfile.mkstemp(suffix='.pdf')

    try:
        with os.fdopen(fd_ht, 'w') as html_file:
            html_file.write(html_code)

        subprocess.check_call(f"wkhtmltopdf --enable-local-file-access {path_ht} {path_pdf}", shell=True)

        with os.fdopen(fd_pdf, 'rb') as pdf_file:
            pdf_binary = pdf_file.read()
    finally:
        os.remove(path_ht)
        os.remove(path_pdf)

    return pdf_binary

def html2img(html_code):
    "Currently returns a single long image"

    fd_ht, path_ht = tempfile.mkstemp(suffix='.html')
    fd_im, path_im = tempfile.mkstemp(suffix='.jpg')

    try:
        with os.fdopen(fd_ht, 'w') as html_file:
            html_file.write(html_code)
        
        subprocess.check_call(f'wkhtmltoimage --enable-local-file-access {path_ht} {path_im}', shell=True)

        print(f'trying to read {path_im}')
        jpg_binary = io.BytesIO()
        with os.fdopen(fd_im, 'rb') as jpg_file:
            jpg_binary.write(jpg_file.read())
    
    finally:
        os.remove(path_ht)
        os.remove(path_im)
    
    yield 0, jpg_binary

def md2img(content : str):
    html_code = md2html(content)
    pdf_binary = html2pdf(html_code)
    # pdf_binary = md2pdf(content)
    yield from pdf2img(pdf_binary)

def md2imgSingle(content : str):
    html_code = md2html(content)
    yield from html2img(html_code)
