import sys
from stats import word_count
from stats import character_count
from stats import print_letters


def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        try:
            file_contents = f.read()
        except Exception as e:
            print(f"bad stuff happened {e}")
    return file_contents

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(f"============ BOOKBOT ============")
    contents = get_book_text(sys.argv[1])


    w_count = word_count(contents)
    print(f"----------- Word Count ----------")
    print(f"Found {w_count} total words")
   
    
    letter_count = character_count(contents)
    print(f"--------- Character Count -------")
    print_letters(letter_count)

    print(f"============= END ===============")

if __name__ == "__main__":
    main()

