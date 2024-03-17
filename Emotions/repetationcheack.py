def check_first_word_repetition(input_file):
    first_words = {}
    repeated_lines = {}

    with open(input_file, 'r',encoding='utf-16') as file:
        for idx, line in enumerate(file, start=1):
            first_word = line.split(':')[0].strip(" '")
            
            if first_word in first_words:
                if first_word in repeated_lines:
                    repeated_lines[first_word].append(idx)
                else:
                    repeated_lines[first_word] = [first_words[first_word], idx]
            else:
                first_words[first_word] = idx

    for word, lines in repeated_lines.items():
        print(f"The first word '{word}' is repeated in lines: {', '.join(map(str, lines))}")

    if not repeated_lines:
        print("No repetition of the first word found in other lines.")

if __name__ == "__main__":
    input_file = 'output_file.txt'  
    check_first_word_repetition(input_file)
