import random
# Rules for Encoding and Decoding
# ---------------------------------
# Encoding Rules:
# 1. For words with 3 or more characters:
#    - Add a random word (from a predefined list) as a prefix and suffix to the original word.
#    - Move the first character of the word to the end.
#    Example:
#    Original word: "hello"
#    Random prefix: "jrd"
#    Random suffix: "def"
#    Encoding Steps:
#      - Move the first character ('h') to the end: "elloh"
#      - Add prefix and suffix: "jrdellohdef"
#    Encoded word: "jrdellohdef"
#
# 2. For words with fewer than 3 characters:
#    - Reverse the word.
#    Example:
#    Original word: "hi"
#    Reversed word: "ih"
#    Encoded word: "ih"
#
# Decoding Rules:
# 1. For encoded words with 3 or more characters:
#    - Remove the random prefix and suffix added during encoding.
#    - Move the last character of the remaining word to the beginning.
#    Example:
#    Encoded word: "jrdellohdef"
#    Random prefix: "jrd"
#    Random suffix: "def"
#    Decoding Steps:
#      - Remove prefix ('jrd') and suffix ('def'): "elloh"
#      - Move the last character ('h') to the beginning: "hello"
#    Decoded word: "hello"
#
# 2. For encoded words with fewer than 3 characters:
#    - Reverse the word.
#    Example:
#    Encoded word: "ih"
#    Reversed word: "hi"
#    Decoded word: "hi"

def randomword():
    """Generate a random word from a predefined list."""
    rand = ["jrd", "def", "ygf", "plk", "lpg", "wer", "der"]
    return random.choice(rand)

def encode_word(word):
    """Encode a word by adding random words and moving the first character to the end."""
    if len(word) >= 3:
        return randomword() + word[1:] + word[0] + randomword()
    else:
        return word[::-1]

def decode_word(word):
    """Decode a word by reversing the encoding process."""
    # Remove the random words added during encoding
    for rand in ["jrd", "def", "ygf", "plk", "lpg", "wer", "der"]:
        if word.startswith(rand):
            word = word[len(rand):]
        if word.endswith(rand):
            word = word[:-len(rand)]
    # Move the last character to the beginning
    if len(word) >= 3:
        return word[-1] + word[:-1]
    else:
        return word[::-1]

def encode_statement(statement):
    """Encode each word in the statement."""
    words = statement.split()
    nword = [encode_word(word) for word in words]
    return ' '.join(nword)

def decode_statement(statement):
    """Decode each word in the statement."""
    words = statement.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

def main():
    """Main function to handle user input and provide encoding/decoding options."""
    while True:
        choice = input("Do you want to (e)ncode or (d)ecode? (e/d): ").strip().lower()
        if choice == 'e':
            statement = input("Enter your statement to encode: ")
            encoded_statement = encode_statement(statement)
            print("Encoded statement:", encoded_statement)
        elif choice == 'd':
            statement = input("Enter your statement to decode: ")
            decoded_statement = decode_statement(statement)
            print("Decoded statement:", decoded_statement)
        else:
            print("Invalid choice. Please enter 'e' to encode or 'd' to decode.")
        
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
