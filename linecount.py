"""
Find out how many lines of code you wrote.
"""

from argparse import ArgumentParser, SUPPRESS
from os import scandir, path


def scan_tree(dir_path):
    """Returns every file in a folder, including all subfolders"""
    try:
        for entry in scandir(dir_path):
            if entry.is_dir(follow_symlinks=False):
                # Scan all sub folders
                yield from scan_tree(entry.path)
            else:
                # Yield all files
                yield entry
    except PermissionError:
        pass


def scan_folder(file_path):
    """Returns every file in a folder without following subfolders"""
    try:
        for entry in scandir(file_path):
            if entry.is_dir(follow_symlinks=False):
                # Ignore subfolders
                continue
            yield entry
    except PermissionError:
        pass


def is_type(file_path, list_of_types):
    """Determine if a file is a certain file type"""
    name, extension = path.splitext(file_path)
    extension = extension.strip('.')
    if extension in list_of_types:
        return True
    return False


def count_lines(file_path):
    """Count the lines in a file"""
    line_number = 0
    with open(file_path) as opened_file:
        for line_number, line in enumerate(opened_file, 1):
            pass
    return line_number


def run():
    """Run the application"""
    # Parse command line arguments
    parser = ArgumentParser(prog="linecount", description="Count the lines in plaintext files")
    parser.add_argument("cwd", type=str, help=SUPPRESS)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--extensions", type=str, nargs="+",
                       help="Count the lines of all files that match these types")
    group.add_argument("-f", "--file", type=str, action="store",
                       help="Count the lines of this file")
    parser.add_argument("-r", "--recursive", action="store_true", help="Include all subfolders")
    args = parser.parse_args()

    if args.file:
        # Count the lines in a single file
        num_lines = count_lines(path.join(args.cwd, args.file))
        print("{} lines in {}".format(num_lines, args.file))
    elif args.extensions:
        # Create a list of extensions
        extensions = list()
        for extension in args.extensions:
            extensions.append(extension)

        # Determines whether or not to scan recursively
        scan = scan_tree if args.recursive else scan_folder

        # Scan all files of matching types
        num_lines = num_files = 0
        print("Scanning...")
        for file_obj in scan(args.cwd):
            if is_type(file_obj.path, extensions):
                num_lines += count_lines(file_obj.path)
                num_files += 1
        print("{} lines in {} files".format(num_lines, num_files))
    else:
        # Invalid arguments
        parser.print_usage()


if __name__ == '__main__':
    run()
