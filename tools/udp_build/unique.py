import argparse
import json

def find_unique_lines(file_path):
    unique_lines = set()
    with open(file_path, 'r') as file:
        for line in file:

            if line.strip().isnumeric():
                print(f"numeric: {line}")
                continue

            unique_lines.add(line)
            print(f"text: {line}")

    return unique_lines

def save_unique_lines(unique_lines, output_file, sort):
    with open(output_file, 'w') as file:
        sorted_lines = list(unique_lines)
        if sort:
            sorted_lines = sorted(unique_lines)

        for line in sorted_lines:
            file.write(line)

def find_and_save_unique_lines(file_path, output_file, sort):
    print(f"Unique lines in {file_path} into {output_file}")

    unique_lines = find_unique_lines(file_path)
    save_unique_lines(unique_lines, output_file, sort)

    print("Done!")

def parse_args():
    parser = argparse.ArgumentParser(description='Find unique lines')

    parser.add_argument('file', help='file to find unique lines')
    parser.add_argument('--output-file', action='store', default='unique.txt', help='output file path')
    parser.add_argument('--sort', action="store_true", dest='sort', default=False, help="sort output data alphabetically")

    return parser.parse_args()

args = parse_args()

find_and_save_unique_lines(args.file, args.output_file, args.sort)
