def count_words(text):
    words = text.split()    # Deleteing spaces
    return len(words)  # Counting the amount of words in the string

def count_characters(text):
    lowered_text = text.lower() # Setting all letters to lowercase
    characters = {} # Initialize a dictionary of occurances
    for char in lowered_text:   # Looping through the text
        if char not in characters:  # Adding the character to the dictionary if not found
            characters[char] = 1
        else:   # Adding +1 occurances if found a character again
            current_occurances = characters[char]
            current_occurances += 1
            characters[char] = current_occurances
    return characters

def sort_occurances(occurances_dict):
    def sort_on_count(dictionary):    # Returns the value of a "count" key in a dictionary
        return dictionary["count"]
    
    sorted_dictionaries = []
    for char in occurances_dict:
        sorted_dictionaries.append(
            {
                "character": char,
                "count": occurances_dict[char]
            }
        )
    sorted_dictionaries.sort(reverse = True, key = sort_on_count)
    return sorted_dictionaries
    