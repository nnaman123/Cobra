#!/usr/bin/env python3
import sys

def run_cobra(code):
    lines = code.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("#"):
            i += 1
            continue

        # print command
        if line.startswith("print "):
            text = line[len("print "):].strip().strip('"')
            print(text)

        # repeat command
        elif line.startswith("repeat "):
            parts = line.split(":")
            count = int(parts[0].split()[1])
            block_indent = " " * 2
            j = i + 1
            block_lines = []
            while j < len(lines) and lines[j].startswith(block_indent):
                block_lines.append(lines[j][len(block_indent):])
                j += 1
            for _ in range(count):
                run_cobra("\n".join(block_lines))
            i = j - 1

        else:
            print(f"Unknown command: {line}")

        i += 1

def main():
    if len(sys.argv) < 2:
        print("Usage: cobra <file.cbr>")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Could not find file {sys.argv[1]}")
        sys.exit(1)
    run_cobra(code)

if __name__ == "__main__":
    main()

