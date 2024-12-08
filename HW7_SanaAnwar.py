import string

# problem 1
def file_copy(in_file, out_file):
    try:
        with open(in_file, 'r') as infile, open(out_file, 'w') as outfile:
            for line in infile:
                outfile.write(line)
        print(f"File copied successfully from {in_file} to {out_file}.")
    except FileNotFoundError:
        print(f"Error: The file {in_file} does not exist.")

# example: file_copy('source.txt', 'destination.txt')

# problem 2
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

# example: file_stats('created_equal.txt')

# problem 3
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

# example: repeat_words('catInTheHat.txt', 'catRepWords.txt')