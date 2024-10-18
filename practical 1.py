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
