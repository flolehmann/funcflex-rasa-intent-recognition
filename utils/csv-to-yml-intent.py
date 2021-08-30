#!/usr/bin/env python3

from argparse import ArgumentParser
import os
import yaml
import pandas as pd


parser = ArgumentParser()
parser.add_argument("-i", "--input_file", type=str,
                    help="Path to CSV input")
parser.add_argument("-c", "--column", type=str,
                    help="Name of input column to process")
parser.add_argument("-x", "--intent_name", type=str,
                    help="Intent name for output")
parser.add_argument("-o", "--output_file",
                    help="Path to YML output")

args = parser.parse_args()

input_file = args.input_file
column = args.column
intent_name = args.intent_name
output_file = args.output_file

if not intent_name:
    intent_name = "intent name"

if not column:
    print("Please specify column name")
    exit()

if not os.path.isfile(input_file):
    print("Path to input file is incorrect")
    exit()

if not output_file:
    print("Path to output file is missing")
    exit()


data = pd.read_csv(input_file)

column_data = data[column]

print(column_data.head())

# - intent: goodbye
#   examples: |

output_list = column_data.dropna().tolist()

result = {
    "examples": output_list,
    "intent": intent_name
}

print(result)

with open(output_file, 'w') as outfile:
    yaml.dump(result, outfile, default_flow_style=False)
