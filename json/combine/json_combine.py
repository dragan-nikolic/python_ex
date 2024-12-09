"""
Combine listed json files

Examples:

$ json_combine a.json b.json

Expected combined json file:
    {
    "B": "BV",
    "A": "AV",
    "C": "CV",
    "D": "DV"
    }

$ json_combine a.json b.json --sort

Expected combined json file is sorted:
    {
    "A": "AV",
    "B": "BV",
    "C": "CV",
    "D": "DV"
    }
"""

import argparse
import json

def merge_json_files(file_paths, output_file, sort=False):
    print(f"Merging {file_paths} into {output_file}")
    merged_data = {}
    for path in file_paths:
        with open(path, 'r') as file:
            data = json.load(file)
            #print(f"Loaded {path}: {data}")
            for item in data:
                if item not in merged_data:
                    merged_data[item] = data[item]
                else:
                    if merged_data[item] != data[item]:
                        print(f"Conflicting item found! {path}: {item}:{data[item]}! Keeping value: {merged_data[item]}")

    if sort:
        merged_data = dict(sorted(merged_data.items()))

    #print(f"merged_data: {merged_data}")

    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=2)

    print("Done!")


def parse_args():
    parser = argparse.ArgumentParser(description='Combine JSON files')

    parser.add_argument('file_paths', nargs='+', help='json files to combine')
    parser.add_argument('--output_file', action='store', default='combined.json', help='output file path')
    parser.add_argument('--sort', action="store_true", dest='sort', default=False, help="sort output data alphabetically by keys")

    return parser.parse_args()

args = parse_args()

merge_json_files(args.file_paths, args.output_file, args.sort)
