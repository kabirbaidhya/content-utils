#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import csv

# Constants
OUTPUT_TEXT_FILE = 'b.txt'
OUTPUT_CSV_FILE = 'b.csv'
DEFAULT_LINE_LENGTH = 30


def read_file(filename):
    ''' Reads a file and returns it's contents. '''
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filename, data):
    ''' Writes data to the file. '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)


def write_csv_file(filename, data):
    ''' Write to CSV format. '''
    lines = data.split('\n')
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        for line in lines:
            writer.writerow([line])


def extract_lines(data, width):
    '''
    Extract lines based on the width from the paragraphs.
    Almost similar to how textwrap works, but not exactly the same.
    '''

    # Normalize
    data = re.sub('(\.|\?)\s+', r'\1', data)

    # Loop
    total_chars = len(data)
    i = 0
    output = ''
    line_length = 0

    while i < total_chars:
        char = data[i]
        line_length = line_length + 1

        if char in ['.', '?']:
            char = char + '\n'
            line_length = 0

        elif char == ' ' and line_length >= width:
            char = '\n'
            line_length = 0

        elif char == '\n':
            line_length = 0

        output = output + char
        i = i + 1

    return output


def main(input):
    ''' The main program. '''
    filename = input[0]
    char_length = DEFAULT_LINE_LENGTH

    if not os.path.exists(filename):
        print('File "{}" does not exist.'.format(filename))
        return

    data = read_file(filename)
    output = extract_lines(data, char_length)

    dir_path = os.path.dirname(os.path.abspath(filename))
    text_output_path = os.path.join(dir_path, OUTPUT_TEXT_FILE)
    csv_output_path = os.path.join(dir_path, OUTPUT_CSV_FILE)

    # Write to file.
    write_file(text_output_path, output)
    write_csv_file(csv_output_path, output)

    print('Output(text) saved to: {}'.format(text_output_path))
    print('Output(csv) saved to: {}'.format(csv_output_path))


# Run it
main(sys.argv[1:])
