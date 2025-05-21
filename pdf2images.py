#!/usr/bin/env python3

import argparse
import os
import sys
import fitz

parser = argparse.ArgumentParser(description="PDF2Images convertor", epilog="(c)Ivaylo Vasilev")
parser.add_argument("pdf", nargs="?", help="specify PDF document")
parser.add_argument("-i", "--images", metavar="png|jpg", default="png", help="set images format: png | jpg")
parser.add_argument("-d", "--directory", metavar="PATH", help="set output directory for images")
parser.add_argument("--version", action="version", version="PDF2Images 2024.5", help="show program version")
args = parser.parse_args()


def main():
    if len(sys.argv) == 1:
        parser.print_usage()
        sys.exit(f"usage: {sys.argv[0]} [pdf] [-i png|jpg] [-d <path>]")
    
    print("")
    print("*         PDF2Images convertor         *")
    print("========================================")
    print("*        (c)2024 Ivaylo Vasilev        *")
    print("")
    pdf_file = args.pdf
    if not os.path.isfile(pdf_file):
        sys.exit(f"[!] PDF file not found at location '{pdf_file}'")
    else:
        extractor(pdf_file)


def extractor(pdf):
    file = pdf.strip('"').split(os.sep)[-1]
    name = file.replace(" ", "-")

    image_fmt = args.images
    if image_fmt == "jpg":
        print("[+] Converting PDF file to JPG images.")
    elif image_fmt == "png":
        print("[+] Converting PDF file to PNG images.")
    else:
        print(f"[!] Wrong format '{image_fmt}'")
        print("[+] Using the default image format: 'png'")
        image_fmt = "png"

    if args.directory:
        dirpath = args.directory
    else:
        dirpath = os.curdir
    
    print("")
    print("Converting ...")

    img = 0
    doc = fitz.Document(pdf)
    if image_fmt == "jpg":
        if not os.path.isdir(f"{dirpath}{os.sep}{name}-JPEG"):
            os.makedirs(f"{dirpath}{os.sep}{name}-JPEG")
        for page in doc.pages():
            pix = page.get_pixmap()
            page_number = page.number + 1
            print(f"Saving Page #{page_number} ...", end="\r")
            pix.pil_save(f"{dirpath}{os.sep}{name}-JPEG/page-{page_number}.jpg", optimize=True, dpi=(600, 600))
            img += 1
    elif image_fmt == "png":
        if not os.path.isdir(f"{dirpath}{os.sep}{name}-PNG"):
            os.makedirs(f"{dirpath}{os.sep}{name}-PNG")
        for page in doc.pages():
            pix = page.get_pixmap()
            page_number = page.number + 1
            print(f"Saving Page #{page_number} ...", end="\r")
            pix.save(f"{dirpath}{os.sep}{name}-PNG/page-{page_number}.png")
            img += 1
    print(f"[+] Converting completed! | Images saved: {img}")


if __name__ == "__main__":
    main()
