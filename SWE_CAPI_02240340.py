################################
#Github Repo: 

#Gayley Choden
#Section 'A'
#02240340
################################

# References
# 1.blackbox.ai (https://www.blackbox.ai/chat/expert-python)
# 2.w3school (https://www.w3schools.com/)
# 3.Chatgpt (https://chatgpt.com/)
# 4.youtube (https://www.youtube.com/)

#PROBLEM
# DOCX.file can't be read
# input file is from online
# The dictionary has many unwanted characters
# Dzongkha words have different unicode and gives wrong format
# white space when seperating the words 
# the word '་' cant act like white space and dilimiter
# everyword is compared, not the wanted words
# when giving positon, st nd rd nd are not assigned properly

#SOLUTION
###############
#Convert DOCX to TXT
import docx2txt as d2t
docx_file = 'dictionary.docx'
txt_file = 'dictionary.txt'
docx = d2t.process(docx_file)
with open(txt_file, 'w', encoding='utf-8') as file:
    file.write(docx)
print ('Converted')

# Question File Download
import wget
url = 'https://csf101-server-cap1.onrender.com/get/input/340'
name= '340.txt'
def download_file(url, name):
        wget.download(url, name)
        print(f"downloaded successfully as {name}")
download_file(url, name)

# Cleaning
file1 = "dictionary.txt"
file2 = "cleaned.txt"
def clean_dictionary(file1, file2):
    cleaned_words = []
    with open(file1, "r", encoding = "utf-8") as file:
        for line in file:
            words = line.split()
            if words:
                dzongkha_word = words[0]
                cleaned_words.append(dzongkha_word)
    with open(file2, "w" , encoding= "utf-8" ) as file:
        for word in cleaned_words:
            file.write(word + "\n")
        print(f"clean words saved to {file2}")
clean_dictionary(file1,file2)

#Read input txt and Spit words
def read_words_with_line_numbers(txt_file):
    words_ = {}
    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.split('་')
                for word_position, word in enumerate(words, start=1):
                    cleaned_word = word.strip().lower()
                    if cleaned_word:  
                        words_[cleaned_word] = (line_number, word_position)
    except FileNotFoundError:
        print(f"Error: The file {txt_file} was not found.")
    return words_

# Main SpellCheck
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