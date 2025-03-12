def word_count(data):
    new_data = data.split() 
    return len(new_data)

def character_count(data):
    word_counter = {}
    word_data = data.split()
    for word in word_data:
        for letter in word:
            new_letter = letter.lower()
            if new_letter in word_counter:
                word_counter[new_letter] += 1
            else:
                word_counter[new_letter] = 1
    return word_counter

def print_letters(data):
    sorted_chars = sorted(data.items(), key=lambda item: item[1], reverse=True)


    for key, value in sorted_chars:
        print(f"{key}: {value}")
