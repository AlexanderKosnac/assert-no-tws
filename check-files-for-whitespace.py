import sys
import os
import re


def parse_file_extensions(extensions_string):
    return tuple([ext.strip() for ext in extensions_string.split(",")])


def files(root, extensions, ignored_dirs):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ignored_dirs]

        for filename in filenames:
            if filename.endswith(extensions):
                yield os.path.join(dirpath, filename)


def file_lines(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                yield (lineno, line)
    except Exception as e:
        print(f"Error reading file {filepath}: {e}", file=sys.stderr)


def has_trailing_whitespace(line):
    return re.search(r"[ \t]+$", line)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Arguments mismatch: {sys.argv[1:]}", file=sys.stderr)
        print(f"Exiting, error code 1.", file=sys.stderr)
        sys.exit(1)

    root_directory = sys.argv[1]
    extensions = parse_file_extensions(sys.argv[2])

    ignored_dirs = [".git"]

    failed = False
    for filepath in files(root_directory, extensions, ignored_dirs):
        print(filepath)
        for lineno, line in file_lines(filepath):
            if (has_trailing_whitespace(line)):
                print(f"{filepath}:{lineno}:{line.rstrip("\n")}")
                failed = True

    sys.exit(1 if failed else 0)
