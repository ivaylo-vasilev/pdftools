import argparse
import os
import sys
import fitz

parser = argparse.ArgumentParser(prog="splitpdf", description="Split PDF documents at given pages", epilog="(c)2024 Ivaylo Vasilev")
parser.add_argument("pdf", nargs="?", help="specify PDF document for splitting")
parser.add_argument("-p", "--pages", metavar="N", type=int, default=5, help="set the number of pages to split")
parser.add_argument("-d", "--directory", metavar="PATH", default=os.curdir, help="set directory for new files")
parser.add_argument("--version", action="version", version="%(prog)s 2024.1rv0-1.21.1", help="show program version")
args = parser.parse_args()


def main():
    if len(sys.argv) == 1:
        print("usage: splitpdf [-h] [-p N] [-d PATH] [--version] [pdf]")
        sys.exit(3)
    
    pdf = args.pdf
    if not os.path.exists(pdf):
        print(f"error: '{pdf}' does not exist")
        sys.exit(1)
    elif os.path.splitext(pdf)[1] != ".pdf":
        print(f"error: '{pdf}' is not a valid PDF document")
        sys.exit(2)
    pages = args.pages

    splitter(pdf, pages)


def splitter(pdf, pages):
    varpages = (pages - 1)
    n = 0

    new_docs = 0

    main_doc = fitz.Document(pdf)
    docpages = int(main_doc.page_count)
    marker = int(main_doc.page_count)

    if pages >= docpages:
        print(f"document '{pdf.split(os.sep)[-1]}' has {docpages} pages")
        print(f"error: cannot split the document at {pages} pages")
        return

    if args.directory != os.curdir:
        if not os.path.exists(args.directory):
            try:
                os.makedirs(args.directory)
            except OSError:
                print("error: could not create directory")
                return
        savedir = (args.directory + os.sep)
    else:
        savedir = (args.directory + os.sep)
    
    print(f"splitting document '{pdf.split(os.sep)[-1]}' at every {pages} page(s) ...")
    print(f"page(s) in document: {docpages}")

    while docpages > 0:
        if docpages == marker:
            varname = (f"{savedir}{os.path.splitext(pdf)[0]}-{n}.pdf")
            temp_doc = fitz.Document()
            temp_doc.insert_pdf(main_doc, from_page=0, to_page=varpages)
            temp_doc.save(varname, garbage=4, deflate=True, clean=True)
            temp_doc.close()
            docpages -= pages
            n += 1
            new_docs += 1
            print(f"[+] saved: {varname}")
        elif docpages < pages:
            varname = (f"{savedir}{os.path.splitext(pdf)[0]}-{n}.pdf")
            temp_doc = fitz.Document()
            temp_doc.insert_pdf(main_doc, from_page=(varpages + 1))
            temp_doc.save(varname, garbage=4, deflate=True, clean=True)
            temp_doc.close()
            new_docs += 1
            print(f"[+] saved: {varname}")
            break
        else:
            varname = (f"{savedir}{os.path.splitext(pdf)[0]}-{n}.pdf")
            temp_doc = fitz.Document()
            temp_doc.insert_pdf(main_doc, from_page=(varpages + 1), to_page=(varpages + pages))
            temp_doc.save(varname, garbage=4, deflate=True, clean=True)
            temp_doc.close()
            varpages += pages
            docpages -= pages
            n += 1
            new_docs += 1
            print(f"[+] saved: {varname}")

    main_doc.close()

    print(f"total new documents saved: {new_docs}")

    return


if __name__ == "__main__":
    main()
