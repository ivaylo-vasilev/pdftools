# PDF tools
CLI tools for working with PDF files.
---
**PDF2Images** - convert **PDF files** into images
 * supported images file formats: **PNG** and **JPEG**
 * supported images quality: up to 600dpi

```
$ pdf2images.py --help

usage: pdf2images [-h] [-i png|jpg] [-q DPI] [-d PATH] [--version] [pdf]

PDF2Images convertor

positional arguments:
  pdf                   specify PDF document

options:
  -h, --help            show this help message and exit
  -i png|jpg, --images png|jpg
                        set images format: png | jpg
  -q DPI, --quality DPI
                        set images quality in DPI (72|96|300|600)
  -d PATH, --directory PATH
                        set output directory for images
  --version             show program version

(c)Ivaylo Vasilev
```

---

**SplitPDF** - split **PDF files** into smaller files by given pages.

```
$ splitpdf.py --help

usage: splitpdf [-h] [-p N] [-d PATH] [--version] [pdf]

Split PDF documents at given pages

positional arguments:
  pdf                   specify PDF document for splitting

options:
  -h, --help            show this help message and exit
  -p N, --pages N       set the number of pages to split
  -d PATH, --directory PATH
                        set directory for new files
  --version             show program version

(c)Ivaylo Vasilev
```

