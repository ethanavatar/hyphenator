# hyphenator

A CLI tool to replace spaces in the name of file(s) with hyphens.

## Installation

This tool is not published to PyPI, so you'll have to install it directly from the repo.
```bash
$ pip install git+https://github.com/ethanavatar/hyphenator.git
```

## Usage

```bash
$ python -m hyphenator --help
usage: hyphenator [-h] {file,dir} ...

Hyphenate the names of files in a directory, a single file, or a list of files.

positional arguments:
  {file,dir}
    file      Hyphenate the name of individual files
    dir       Hyphenate the names of all files in a directory

options:
  -h, --help  show this help message and exit
```

### Convert a single file

```bash
$ python -m hyphenator file path/to/file
```

### Convert all files in a directory

```bash
$ python -m hyphenator dir path/to/dir/of/files
```
