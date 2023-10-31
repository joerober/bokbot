#!/usr/bin/env python3 

#FILE=<path_to_file> # TODO: cmd line argument

def categorize_file(filename):
    get_category = lambda extension: {
        ".txt": "Text",
        ".docx": "Document",
        ".py": "Code",
    }.get(extension, "Unknown")

    return get_category(filename[filename.rfind(".") :])

def count_words(words): 
    all_words=words.split() 
    return len(all_words) 

def get_doc_text(path_to_text):
    with open(path_to_text, "r") as f:
        file_contents = f.read() 
    return file_contents 

def count_letters(words): 
    count={} 
    for i in words.lower(): 
        count[i]=count.get(i, 0) + 1 
    return count

def get_report(path_to_doc): 
    doc_text=get_doc_text(path_to_doc) 
    char_count=count_letters(doc_text) 
    char_lst=list(char_count) 
    char_lst.sort() 
    print(f'\n--- Begin report of {FILE} ---\n')
    print(f'{count_words(doc_text)} found in the document\n')

    for i in char_lst: 
        if i.isalpha():
            print(f"The '{i}' character was found {char_count[i]} times")
    print(f'\n--- End Report ---\n')

#print(file_contents)
#print(count_words(get_doc_text('books/frankenstein.txt'))) 
#all_text=get_doc_text(FILE) 
#print(count_letters(all_text))

get_report(FILE) 