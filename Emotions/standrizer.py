def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        words = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as file:
        for word in words:
            word = word.strip()
            if len(word.split()) == 1:  # Check if the line contains only one word
                modified_word = f"'{word}': "
                modified_word2 = f"{modified_word}'suicidal',"
                file.write(modified_word2 + '\n')

if __name__ == "__main__":
    process_file('wordsin.txt', 'emotionout.txt')
