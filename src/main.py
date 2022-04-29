import os
import argparse

from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File header injection tool")
    parser.add_argument("-e", "--ext", default=".py", help="File extension (ex: .py, .c, .java)")
    parser.add_argument("-c", "--content", default="header.txt", help="Content of the header need to be added")
    parser.add_argument("-x", "--exclude", default="venv|data", help="Exclude folder (ex: venv|data)")
    parser.add_argument("-r", "--revert", default=False, action="store_true", help="Revert header with the given content")
    args = parser.parse_args()

    with open(args.content, "r") as stream:
        header = stream.read()

    for path in Path(".").rglob(f"*{args.ext}"):
        with open(path, "r+") as stream:
            content = stream.read()
            if args.revert is True:
                stream.truncate(0)
                stream.seek(0, 0)
                stream.write(content.replace(f"{header}\n", ""))
            else:
                stream.seek(0, 0)
                stream.write(f"{header}\n{content}") 
