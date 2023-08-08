def is_cyclone_word(word):
    # Convert the word to lowercase for case-insensitive comparison
    word = word.lower()
    
    # Check if the word has at least 3 characters
    if len(word) < 3:
        return False
    
    # Create two pointers for cyclic pattern comparison
    left = 0
    right = len(word) - 1
    
    while left < right: # left kieu gi cx nho hon right (tru truong hop tu co 2 chu)
        # Check if the characters are not in alphabetical order
        if word[left] > word[right]:
            return False
        
        # Move the pointers in a cyclic pattern
        left += 1
        right -= 1
        
        # Skip non-alphabetic characters
        while not word[left].isalpha():
            left += 1
        while not word[right].isalpha():
            right -= 1
    
    return True

def main():
    word = "settled"
    result = is_cyclone_word(word)
    print(f"{word} is a cyclone word: {result}")

if __name__ == "__main__":
    main()