# About PdfMerger

* This is a simple script written in **[Python](python.org "Python Website")** that allows you to merge multiple PDF files using the **[PyPDF2](https://pypdf2.readthedocs.io/en/latest/ "PyPDF2 documentation")** module.
* This script uses the **[argparse](docs.python.org/3/library/argparse.html "argpasre documentation")** module which means you can pass args to the script.

# Requirements

* You shoud have **[Python](https://www.python.org/downloads/ "Download Python")** installed in your machine.
* You should install the **[PyPDF2](https://pypdf2.readthedocs.io/en/latest/user/installation.html "PyPDF2 installation")** module.

# Usage

```bash
python pdfMerger.py -h
```

# Options

* **-d:** here you can specify the input directory (default is current directory)
* **-o:** here you can specify the output directory (default is current directory)
* **-n:** set a name for the output merged file (default is today's date + "_merger.pdf" )

# Example

* **Input Directory:** "pdf_files"
* **Output Directory:** "merged_files"
* **Output Merged File Name:** "Bingo.pdf"

### Command line

```bash
python pdfMerger.py -d "pdf_files" -o "merged_files" -n "Bingo.pdf"
```

# Screenshot
* See the [Result](https://github.com/lakehalmehdi/PdfMerger/raw/main/Screenshot.png "PDF Merger")

**Happy merging !**

