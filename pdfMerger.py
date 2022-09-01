import os
import sys

from PyPDF2 import PdfFileMerger
from datetime import datetime
import argparse
import random
import string

# Arg Parser
parser = argparse.ArgumentParser()
parser.add_argument("-d", metavar="--dir", nargs=1, help="Specify The Input Directory (Default = current directory)",
                    default=os.curdir)
parser.add_argument("-o", metavar="--output", nargs=1, help="Specify The Output Directory (Default = current directory)",
                    default=os.curdir)
parser.add_argument("-n", metavar="--name", nargs=1, help="Specify The Output File Name",
                    default=str(datetime.today().strftime('%Y_%m_%d')) + "_merged.pdf")
args = parser.parse_args()


# Merge Function
def merge_action(input_dir, output_dir, file_name):
    # Pdf File Merger
    merger = PdfFileMerger()

    # Convert Args
    input_dir = convert_arg(input_dir)
    output_dir = convert_arg(output_dir)
    file_name = convert_arg(file_name)
    letters = string.ascii_lowercase

    # Check if file exits with the same name
    if os.path.exists(output_dir + "/" + file_name):
        f_name = random.choice(letters) * 3 + "_" + file_name
    else:
        f_name = file_name
    output = output_dir + "/" + f_name
    print(f'Start looking for PDF Files inside "{input_dir}"')

    # Search all PDF Files then Append Them in the Merger
    for files in os.listdir(input_dir):
        if files.endswith(".pdf"):
            merger.append(files)

    # Check if PDF files are available
    if len(merger.inputs) == 0:
        print("PDF Files not found :/")
        sys.exit()

    # Printing (Total PDF / Total Merged Pages / Output Directory)
    print(f'Total PDF Files Found: "{len(merger.inputs)}"')
    print(f'Total Number Of Merged Pages: "{merger.id_count}"')
    print(f'Output Directory: "{output_dir}"')

    merger.write(output)
    merger.close()
    print("\nDone !")


# Deal with args
def convert_arg(arg):
    if type(arg) == list:
        return arg[0]
    else:
        return arg


# Run the script
if __name__ == '__main__':
    print("""
        ********************************
        * PDF Merger v1.0 By M.LAKEHAL *
        ********************************
    """)
    merge_action(args.d, args.o, args.n)
