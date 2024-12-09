# Sana Anwar
# CS 100 H FALL 2023
# Homework 7 - Files

"""
Problem 1: Write a function file_copy that takes two string parameters (in_file and out_file) and copies the content of in_file into out_file.
Assume that in_file exists before file_copy is called.

Problem 2: Write a function named file_stats that takes one string parameter (in_file) that is the name of an existing text file. 
The function file_stats should calculate three statistics about in_file: the number of lines it contains, the number of words and the number of characters, 
and print the three statistics on separate lines. 

Problem 3: Write a function named repeat_words that takes two string parameters:
    - in_file: the name of an input file that exists before repeat_words is called
    - out_file: the name of an output file that repeat_words creates

Assume that the input file is in the current working directory and write the output file to that directory.
For each line of the input file, the function repeat_words should write to the output file all of the words that appear more than once on that line. 
Each word should be lower-cased and stripped of leading and trailing punctuation. 
Each repeated word on a line should be written to the corresponding line of the output file only once, regardless of the number of times the word is repeated.
"""

import string

# Problem 1
def file_copy(in_file, out_file):
    try:
        with open(in_file, 'r') as infile, open(out_file, 'w') as outfile:
            for line in infile:
                outfile.write(line)
        print(f"File copied successfully from {in_file} to {out_file}.")
    except FileNotFoundError:
        print(f"Error: The file {in_file} does not exist.")

# Problem 2
def file_stats(in_file):
    try:
        with open(in_file, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
        
        print(f"lines {num_lines}")
        print(f"words {num_words}")
        print(f"characters {num_chars}")
    except FileNotFoundError:
        print(f"Error: The file {in_file} does not exist.")

# Problem 3
def repeat_words(in_file, out_file):
    try:
        with open(in_file, 'r') as infile, open(out_file, 'w') as outfile:
            for line in infile:
                words = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
                seen = set()
                repeats = set()
                for word in words:
                    if word in seen:
                        repeats.add(word)
                    else:
                        seen.add(word)
                outfile.write(' '.join(repeats) + '\n')
        print(f"Repeated words written to {out_file}.")
    except FileNotFoundError:
        print(f"Error: The file {in_file} does not exist.")