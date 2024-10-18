
def read_words_with_line_numbers(txt_file):
    words_ = {}
    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.split('་')
                for word_position, word in enumerate(words, start=1):
                    cleaned_word = word.strip().lower()  # Normalize to lowercase
                    if cleaned_word:  
                        words_[cleaned_word] = (line_number, word_position)
    except FileNotFoundError:
        print(f"Error: The file {txt_file} was not found.")
    return words_

def check_spelling_with_line_numbers(file_txt, dictionary_txt):
    text_words_with_lines = read_words_with_line_numbers(file_txt)
    dictionary_words = set(read_words_with_line_numbers(dictionary_txt).keys())  
    incorrect_words = {word: text_words_with_lines[word] for word in text_words_with_lines if word not in dictionary_words}
    return incorrect_words

ordinal = lambda n: f"{n}{'th' if 10<= n % 100 <= 20 else {1:'st', 2:'nd', 3:'rd'}.get (n%10,'th')}"

text_file = '340.txt' 
dictionary_file = 'cleaned.txt'
misspelled = check_spelling_with_line_numbers(text_file, dictionary_file)

print("Incorrect Words and Their Line Numbers:")
for word, (line, position) in misspelled.items():
    print(f"line {line}, {ordinal(position)} word '{word}'is incorrect")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python dzongkha_spell_checker.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    dictionary_file = "dictionary.txt"
    check_spelling_with_line_numbers(text_file, dictionary_file)