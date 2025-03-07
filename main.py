from stats import  count_words, count_characters, sort_occurances
import sys

def get_book_text(path_to_file):
    # Reading the file
    file_as_string = ""
    with open(path_to_file) as file:
        # Assigning to a string the file contents
        file_as_string = file.read()
    return file_as_string

def print_occurances(occurance_list):
    for dict in occurance_list:
        print(f"{dict["character"]}: {dict["count"]}")
        

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_route = sys.argv[1]
    
    # Start print format
    print("============ BOOKBOT ============")
    
    # text to string
    frankenstein = get_book_text(book_route)
    print(f"Analyzing book found at {book_route}...")
    
    # counting words in the book
    print("----------- Word Count ----------")
    total_words = count_words(frankenstein)
    print(f"Found {total_words} total words")
    
    # Counting the occurances of each character in the book
    print("--------- Character Count -------")
    occurances = count_characters(frankenstein)
    occurances_list = sort_occurances(occurances)
    print_occurances(occurances_list)

    print("============= END ===============")
    
main()