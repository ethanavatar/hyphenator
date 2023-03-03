
import os
import sys
import argparse


def hyphenate_files(file: list[str]):
    for f in file:
        if not os.path.isfile(f):
            print(f"{f} is not a file")
            continue

        filepath = os.path.abspath(f)

        os.rename(filepath, filepath.replace(" ", "-"))

def hyphenate_dir(dir: str):
    path = os.path.abspath(dir)
    files = os.listdir(path)

    for f in files:
        f = os.path.join(path, f)

    hyphenate_files(files)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="hyphenator", description="Hyphenate the names of files in a directory, a single file, or a list of files.")
    subparsers = parser.add_subparsers(dest="command")

    # Create the parser for the "file" command
    f = subparsers.add_parser("file", help="Hyphenate the name of individual files")
    f.add_argument("input", help="The input file to hyphenate (in-place)", nargs="+")

    # Create the parser for the "dir" command
    d = subparsers.add_parser("dir", help="Hyphenate the names of all files in a directory")
    d.add_argument("input", help="The input directory to hyphenate (in-place)")

    args = parser.parse_args()

    if args.command == "file":
        print (args.input)

    elif args.command == "dir":
        print (args.input)

    else:
        parser.print_help()