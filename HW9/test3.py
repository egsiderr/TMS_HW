def most_common_word_in_line(line):
    words = line.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    most_common_word = max(word_count, key=word_count.get)
    count = word_count[most_common_word]
    
    return most_common_word, count

def operations_with_files(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            most_common_word, count = most_common_word_in_line(line)
            outfile.write(f"{most_common_word} {count}\n")

input_file = 'file.txt'
output_file = 'outputfile.txt'
operations_with_files(input_file, output_file)